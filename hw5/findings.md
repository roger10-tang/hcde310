# HW5 findings

## 1. Drawing: one search for "Monet"
(photo here)

## 2. Two questions about the code
1. what do or "" and .strip() do?
2. What happens if the API returns an HTTP error

## 3. Checks (4 or more, at least 2 as pytest tests)
| # | Check | Pass or fail |
|---|---|---|
| 1 | Home page shows the search form| Pass |
| 2 | Spaces-only input shows an empty-search message| Pass |
| 3 | Searching 'Monet' shows 1–10 artworks| Pass |
| 4 | Searching 'rogerrrr' shows a no-results message| Fail |

## 4. AI review
What it found that I missed: If the API request fails, the app shows the raw error message and still returns HTTP 200. My checks did not cover API failures.
What it got wrong: I didn’t find a clear factual mistake. The AI flagged the form label and no-results message as things to verify. I checked the templates and found that both are already there.
Answers to my two questions, in my own words: 
1. `or ""` defaults to an empty string. `.strip()` trims whitespace.
2. `raise_for_status()` raises an exception, and Flask catches it and shows an error message.

## 5. My fix
What was wrong:
What I changed:
How I checked it works:
Commit before: (hash)  Commit after: (hash)

## 6. Can we ship it? (100–150 words)
Yes or no, and why:

One thing my HW4 does better:
One thing the AI's app does better:

AI use goes in `ai_use.md` (the five points on the AI Use Card).
