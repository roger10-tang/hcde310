import requests

URL = "https://api.artic.edu/api/v1/artworks/search"
FIELDS = "title,artist_title,date_display"

# Send the keyword to the HW3 API and return its artwork list.
# Return None if the request fails.
def search_art(term):
    """Take a search term and return artworks, or None on an API error."""
    try:
        response = requests.get(URL, params={"q": term, "fields": FIELDS},
                                headers={"AIC-User-Agent": "HCDE310 student project"}, timeout=10)
        if response.status_code != 200:
            return None
        return response.json()["data"]
    except (requests.RequestException, ValueError, KeyError):
        return None
