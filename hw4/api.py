import requests

URL = "https://api.artic.edu/api/v1/artworks/search"
FIELDS = "title,artist_title,date_display"

# AI-written
# Send the keyword to the HW3 API and return its artwork list.
# Return None if the request fails.
def search_art(term):
    """Take a search term and return artworks, or None on an API error."""
    try:
        # Send the search word to the API. Wait up to 10 seconds.
        response = requests.get(URL, params={"q": term, "fields": FIELDS},
                                headers={"AIC-User-Agent": "HCDE310 student project"}, timeout=10)
        # Only use the data if the request worked.
        if response.status_code != 200:
            return None
        # The artwork list is inside "data".
        return response.json()["data"]
    # Let the route show a message if the request or data fails.
    except (requests.RequestException, ValueError, KeyError):
        return None
