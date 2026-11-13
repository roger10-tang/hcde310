# HW5 AI use

## Stage

Homework 5 lists **Stage 4 – Spec first**. In this conversation, I used Codex to review the starter Flask app and answer follow-up questions about error handling and search results.

## AI conversation

The [appendix](#appendix-codex-review-and-follow-up-questions) contains the Step 4 prompt with the original Python code, Codex’s review, and the follow-up questions and answers from this conversation.

## What AI helped with

- **Flask code review.** Codex pointed out that the starter app displayed the original API error and returned HTTP 200. It also flagged debug mode, unchecked API response data, and broad artwork searches. It suggested checking the form label, error feedback, and image descriptions in the templates.
- **HTTP 502 and error testing.** Codex explained why an unusable upstream response can return HTTP 502. It provided a Flask test-client example that checks the status, looks for a friendly message, and verifies that the original error stays out of the HTML.
- **Search results and the shipping decision.** Codex checked the museum API directly. All ten results for `Monet` were credited to Claude Monet, while `rogerrrr` returned works by unrelated artists. It suggested checking each artwork’s artist ID and holding off on shipping until an unknown name shows a clear no-results message with zero artwork cards.
- **AI-use disclosure.** Codex drafted this summary and reflection and included the review and follow-up exchanges below.

## Reflection

I expected `rogerrrr` to return no results, but it returned ten artworks. Next time, I’d check who made each artwork before calling the search a pass.

## Appendix. Codex review and follow-up questions

### Turn 1

**My message**

Review this Flask app for bugs, missing error handling, accessibility and security problems. For each one, point to the line.

```python
from flask import Flask, render_template, request

from api import get_artworks

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/results", methods=["GET", "POST"])
def results():
    artist = (request.values.get("artist") or "").strip()
    if not artist:
        return render_template("home.html", message="No search term entered.")
    try:
        artworks = get_artworks(artist)
    except Exception as e:
        return render_template("home.html", message=f"Something broke the request: {e}")
    return render_template("results.html", artist=artist, artworks=artworks)


if __name__ == "__main__":
    app.run(debug=True)

# api.py
import requests

URL = "https://api.artic.edu/api/v1/artworks/search"
FIELDS = "id,title,artist_title,date_display,image_id"


def get_artworks(artist):
    params = {"q": artist, "fields": FIELDS, "limit": 10}
    headers = {"User-Agent": "hcde310-artist-search/1.0"}
    response = requests.get(URL, params=params, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json().get("data", [])[:10]
```

**AI progress message**

I’ll review the pasted code line by line and check the Flask and Art Institute documentation where framework or API behavior affects a finding.

**AI reply**

I treated the pasted code as two files, `app.py` and `api.py`, and numbered each from its first import, including blank lines. This was a static review. The template references below point to the Python lines that render them.

### Bugs, error handling, and security

| Line | Finding |
|---|---|
| `app.py:26` | **High if exposed · Debugger enabled.** Running this file directly starts Flask’s development server with the interactive debugger, which can execute Python code if exposed. Keep debug mode local and use a production WSGI server for deployment. [Flask debugging docs](https://flask.palletsprojects.com/en/stable/debugging/) |
| `app.py:18–21` | **Internal errors are exposed and returned as HTTP 200.** If the template displays `message`, `str(e)` can reveal upstream URLs and other diagnostic details. The broad catch also masks programming errors. Catch expected API failures, log the details server-side, and give users a plain-language message with an appropriate status, such as `504` for an upstream timeout. Let unexpected exceptions reach Flask’s 500 handler. |
| `api.py:12` | **The API response shape is unchecked.** A missing `data` key silently looks like zero matches. A `null` value or a top-level JSON array can raise an exception. Check that the payload is an object containing a `data` list of artwork objects, and treat malformed responses as upstream failures. [Requests response handling](https://docs.python-requests.org/en/latest/user/quickstart/#json-response-content) |
| `api.py:8` | **Artist search can return works by other artists.** The API’s `q` parameter searches artwork metadata broadly. If the form promises artist search, query an artist field or resolve the artist and filter by ID. [Art Institute search docs](https://api.artic.edu/docs/) |
| `app.py:13–15` | **A URL parameter can override the submitted form value.** On POST, `request.values` checks the query string before form data. Use `request.args` for GET and `request.form` for POST, or use GET alone for this read-only search. [Werkzeug request implementation](https://raw.githubusercontent.com/pallets/werkzeug/main/src/werkzeug/wrappers/request.py) |
| `app.py:15–19`, `api.py:10–11` | **Search traffic can exhaust upstream quota or occupy app workers.** The shown code accepts any nonblank query length and makes a synchronous API call for every search. Cap the term length, rate-limit the route if public, and handle upstream `429` with a clear retry-later message. Requests’ `timeout=10` is an inactivity timeout, so a call can take longer than ten seconds overall. [Art Institute API limits](https://api.artic.edu/docs/#authentication), [Requests timeouts](https://docs.python-requests.org/en/latest/user/quickstart/#timeouts) |

### Accessibility checks

The HTML templates were absent from the snippet, so these are checks to verify in the rendered pages.

- **`app.py:10, 17, 21` · Search form and feedback.** Give the input a visible, associated label. For an empty submission, display a specific instruction such as “Enter an artist name” and associate it with the field. Make service errors easy to find after the page reloads. [W3C form notifications](https://www.w3.org/WAI/tutorials/forms/notifications/)
- **`app.py:22`, `api.py:4` · Results and artwork images.** Verify that zero matches produce an explicit message. If the page displays artwork images, the requested fields omit the museum’s `thumbnail.alt_text`. Request it, use it where available, and handle missing descriptions and image IDs. [Art Institute artwork data](https://api.artic.edu/docs/), [W3C image alternatives](https://www.w3.org/WAI/tutorials/images/decision-tree/)

### Turn 2

**My message**

Why is HTTP 502 appropriate when the artwork API fails, and how can I verify that the page shows a friendly message without exposing the original error?

**AI progress message**

I’ll check the HTTP status definitions and show how to verify the rendered response with Flask’s test client.

**AI reply**

**Use `502 Bad Gateway` when Flask gets an unusable response from the artwork API**, such as invalid JSON. The user submitted a valid search, but Flask couldn’t complete it because the upstream response was unusable. Use `504 Gateway Timeout` when the API takes too long to respond, and `500 Internal Server Error` for an unexpected bug in Flask’s own code. [HTTP Semantics, RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.6)

At `app.py:20–21`, handle the expected upstream failure by logging the exception server-side and rendering `home.html` with a fixed message and an explicit `502` status. For example, use “The artwork search is temporarily unavailable. Please try again later.”

Verify the actual HTML with Flask’s test client. Patch `app.get_artworks` because that’s the name the route calls. This test uses the real template and simulates invalid upstream JSON without contacting the museum. [Flask test client docs](https://flask.palletsprojects.com/en/stable/testing/#sending-requests-with-the-test-client)

```python
import app as app_module
from requests.exceptions import JSONDecodeError


def test_invalid_artwork_response_shows_friendly_error(monkeypatch):
    private_detail = "UPSTREAM_DIAGNOSTIC_SENTINEL"

    def fail_search(artist):
        raise JSONDecodeError(private_detail, "", 0)

    monkeypatch.setattr(app_module, "get_artworks", fail_search)

    with app_module.app.test_client() as client:
        response = client.get("/results", query_string={"artist": "Monet"})

    html = response.get_data(as_text=True)
    assert response.status_code == 502
    assert "The artwork search is temporarily unavailable." in html
    assert private_detail not in html
```

The pasted handler currently returns `200`. After the fix, the test checks that the error status and friendly text reach the browser and that the original diagnostic stays out of the response body. To verify the message is **visible**, also check the rendered page in a browser with the same simulated failure.

### Turn 3

**My message**

Searching for `Monet` and `rogerrrr` both returned ten artworks. What should I check to see whether the results actually match the requested artist? What result would make you hold off on shipping?

**AI progress message**

I’ll compare the museum API’s results for both terms and check the artist attribution on the returned records.

**AI reply**

**I’d hold off shipping this as an artist search.** I reproduced both queries against the museum API using the parameters in `api.py:8`. All ten `Monet` results were credited to Claude Monet. The ten `rogerrrr` results were credited to other artists, including Edward Hopper and Grant Wood. A strict artist-name filter returned zero for `rogerrrr`. [Monet API response](https://api.artic.edu/api/v1/artworks/search?q=Monet&fields=id%2Ctitle%2Cartist_title%2Cdate_display%2Cimage_id&limit=10), [rogerrrr API response](https://api.artic.edu/api/v1/artworks/search?q=rogerrrr&fields=id%2Ctitle%2Cartist_title%2Cdate_display%2Cimage_id&limit=10), [Strict filter response](https://api.artic.edu/api/v1/artworks/search?query%5Bterm%5D%5Bartist_title.keyword%5D=rogerrrr&limit=10)

Check the **artist attribution on every result**. `artist_title` is enough for a quick spot check. For a release test, request `artist_id` and compare it with the selected artist’s museum ID. Claude Monet is `35809`. If the app includes co-creators, check membership in `artist_ids` as well. The ten-result cap makes the count a poor signal for whether the search worked. [Claude Monet ID-filtered response](https://api.artic.edu/api/v1/artworks/search?query%5Bterm%5D%5Bartist_id%5D=35809&fields=id%2Ctitle%2Cartist_title%2Cartist_id&limit=10), [Artwork field definitions](https://api.artic.edu/docs/#artworks-2)

I’d ship once the app passes both checks end to end: **a known artist returns at least one work and every result has the expected attribution**, and **an unknown name shows “No matching artists” with zero artwork cards**. Apply the artist filter upstream before the ten-result limit so unrelated records can’t crowd out real matches.

### Turn 4

**My message**

Searching for `Monet` and `rogerrrr` both returned ten artworks. What should I check to see whether the results actually match the requested artist? What result would make you hold off on shipping?

**AI reply**

Check the **artist credited on each artwork**. In the API response, inspect `data[].artist_title`. For a release test, request `artist_id` and compare it with the intended artist’s museum ID. Claude Monet’s is `35809`. [Museum API response filtered by Monet’s ID](https://api.artic.edu/api/v1/artworks/search?query%5Bterm%5D%5Bartist_id%5D=35809&fields=id%2Ctitle%2Cartist_title%2Cartist_id&limit=10)

I reproduced both searches against the museum API. All ten `Monet` results were credited to Claude Monet. The `rogerrrr` results included works by Edward Hopper and Grant Wood. That’s enough to **hold off shipping** an artist search. The app caps results at ten, and `q` searches artwork metadata broadly. [Museum response for `rogerrrr`](https://api.artic.edu/api/v1/artworks/search?q=rogerrrr&fields=id%2Ctitle%2Cartist_title&limit=10), [Museum search documentation](https://api.artic.edu/docs/)

I’d require two checks through the actual search page before shipping.

- **`Claude Monet`** returns at least one artwork, and every card is backed by a record attributed to him.
- **`rogerrrr`** shows a clear “No matching artists” message and zero artwork cards.
