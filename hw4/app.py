from flask import Flask, render_template, request

from api import search_art

app = Flask(__name__)

# Show the search form on the home page
@app.route("/")
def home():
    return render_template("home.html")

# AI-written
# Get the search term from the form
@app.route("/results")
def results():
    """Take a keyword and return a results page, or a message if empty."""
    # Read the keyword and remove spaces at both ends.
    keyword = request.args.get("keyword", "").strip()
    # If the search term is empty, then show a message
    if keyword == "":
        return render_template("home.html", message="Please enter a keyword.")
    # Get real artworks instead of the fake data used in the first version.
    artworks = search_art(keyword)
    # None means the API failed; an empty list means no matches.
    if artworks is None:
        return render_template("home.html", message="Search is unavailable. Please try again later.")
    if len(artworks) == 0:
        return render_template("home.html", message="No artworks found. Try another keyword.")
    # Show the artworks on the results page.
    return render_template("results.html", artworks=artworks, keyword=keyword)
