# HW3 Part 2 + Part 3 + Part 4
#
# Instructions: README.md in this folder (same as the assignment on Canvas).

import requests

FIELDS = "id,title,artist_title,artist_display,date_display"

# Functions go here (above the code that runs)


def count_by_artist(artworks):
    """Takes an artwork list and returns a dictionary of counts by artist."""
    counts = {}
    for artwork in artworks:
        artist = artwork.get("artist_title") or "Unknown"
        counts[artist] = counts.get(artist, 0) + 1
    return counts


# AI-written
def save_results(artworks, filename):
    """Take artwork dictionaries and a filename, write one artwork per line, and return None."""
    with open(filename, "w", encoding="utf-8") as file:
        for artwork in artworks:
            title = artwork.get("title") or "Unknown title"
            artist = artwork.get("artist_title") or "Unknown artist"
            date = artwork.get("date_display") or "Unknown date"
            file.write(f"{date}, {title}, {artist}\n")


term = input("Search the Art Institute for: ")

url = "https://api.artic.edu/api/v1/artworks/search"      # TODO: the search URL from step 2
params = {"q": term, "fields": FIELDS}   # TODO: q (the search term) and fields (FIELDS)
headers = {"AIC-User-Agent": "HCDE310 student project"}
response = requests.get(url, params=params, headers=headers)

# TODO step 3: check response.status_code before you use the data

if response.status_code == 200:
    data = response.json()
    artworks = data["data"]
    save_results(artworks, "results.txt")

    if not artworks:
        print("No artworks found")
    else:
        for artwork in artworks:
            title = artwork.get("title") or "Unknown title"
            artist = artwork.get("artist_title") or "Unknown artist"
            year = artwork.get("date_display") or "Unknown date"
            artwork_id = artwork.get("id")
            score = artwork.get("_score")

            print(f"{title} - {artist} ({year})")
            print(f"ID: {artwork_id}")
            print(f"Score: {score}")
            print()
        print(count_by_artist(artworks))
else:
    print(f"Search failed: {response.status_code} {response.reason}")

# TODO steps 4-5: loop over the results and print each one (reuse your HW2 printing code),
#                 print a default for null fields, and print a helpful message if there are no results

