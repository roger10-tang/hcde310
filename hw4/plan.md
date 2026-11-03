Search page sketch: still need to add.
Results page sketch: still need to add.

I'll use title, artist_title, and date_display from the API's data list to show the artwork's title, artist, and date.
The / route takes a visit to the home page and shows home.html with a search form. I'll check that the form appears and that submitting a keyword goes to /results.
The API search function takes a keyword and returns artworks, or reports an API error. I'll try "cat", a search with no results, and a wrong API URL. I'll also change the URL back after checking the error.
The /results route takes the keyword from the form and shows results.html with the artworks or a message. I'll check a normal search, an empty search, and an API error. The page should also show a helpful message for no results and fallback text for missing artwork fields.

Browser checks (fake data): "cat" showed Sample artwork - Sample artist (1900): pass. Back to search returned home: pass. Empty search showed "Please enter a keyword.": pass. Checked by the AI assistant.
