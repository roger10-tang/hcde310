# HW3 Part 1 – Read the response first

AI Use: Stage 2 (Tutor)

Open `sample_response.json` (a saved Art Institute of Chicago search). In `notes.md`:

---

## 1. The total number of results is at `data["pagination"]["total"]`. What's the path to the first artwork's title?
data["data"][0]["title"]

## 2. Find 3 more fields you'd want to show a user, and their paths
Search score: data["data"][0]["_score"]
Artwork ID: data["data"][0]["id"]
Artwork date: data["data"][0]["date_display"]

## 3. Which fields are `null` for some works?
artist_title

## 4. Predict
*open `fetch.py` and read it, but don't change anything yet. What do you think will happen when you run it?*
I think the program will ask for a search term and then produce an error because the URL is empty

## 5. Run it
*run `python3 fetch.py`. When it asks for a search term, type a word (like `cat`) and press Enter. What actually happened? Read the traceback bottom line first: what went wrong, and which line of your file caused it?*
After I entered `cat` the program raised a `MissingSchema` error because the URL was empty. Line 16 of `fetch.py`, `response = requests.get(url, params=params)` triggered the error. Which matched my prediction.