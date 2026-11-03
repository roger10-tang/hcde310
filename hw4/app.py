from flask import Flask, render_template, request

app = Flask(__name__)

# Show the search form on the home page
@app.route("/")
def home():
    return render_template("home.html")

# Get the search term from the form
@app.route("/results")
def results():
    """Take a keyword and return a results page, or a message if empty."""
    keyword = request.args.get("keyword", "").strip()
    # If the search term is empty, then show a message
    if keyword == "":
        return render_template("home.html", message="Please enter a keyword.")
    # Use fake artwork data first
    artworks = [
        {"title": "Sample artwork", "artist_title": "Sample artist", "date_display": "1900"}
    ]
    # Show the artworks on the results page
    return render_template("results.html", artworks=artworks, keyword=keyword)
