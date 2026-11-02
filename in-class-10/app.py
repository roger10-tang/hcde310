# app.py: the routes for the books app.
# SKELETON: the whole path works (form → /results → results page) with fake data.
# Next: replace one piece at a time, and commit each time something works.
from flask import Flask, render_template, request   # request (Flask), not requests!
from api import get_books

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/results")
def results():
    # 1. Read the search term from the form
    author = request.args.get("author_search", "").strip()

    # 2. Empty input? → home page + message (check BEFORE calling the API)

    if not author:
        return render_template("home.html", message="Enter an author name to find books.")

    # 3. Call the API (fake data for now)
    books = get_books(author)

    # 4. API error? (get_books returned None) → home page + message

    if books is None:
        return render_template("home.html", author=author, message="We could not reach the book service. Please try again in a moment.")

    # 5. No results, or nothing useful to show? → home page + message

    # Skip entries without a usable title; a missing year is still useful.
    books = [book for book in books
             if isinstance(book, dict) and isinstance(book.get("title"), str)
             and book["title"].strip()]
    if not books:
        return render_template("home.html", author=author, message="No books found. Check the author spelling or try another author.")

    # 6. Otherwise → results page
    return render_template("results.html", books=books, author=author)
