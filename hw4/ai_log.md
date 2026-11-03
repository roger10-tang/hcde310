I'm building a small Flask app for searching artworks. My home route already renders templates/home.html, but the file is empty.

I need a page title, a search input with a label, and a search button. The form should use GET to submit the keyword to /results.

How should I write this form? Please guide me with simple hints so I can write it myself. Don't add CSS or extra features.







14:19






In templates/home.html, try building these pieces in order:
1. Add a heading using an h1 element, such as “Search artworks.”
2. Add a form element. Set its action to /results and its method to get.
3. Inside the form, add a label saying “Keyword.” Give its for attribute the value keyword.
4. Add an input with type="text", id="keyword", and name="keyword". The id connects it to the label; the name identifies the value sent to Flask.
5. Add a button with type="submit" and the text “Search.”
6. Close the form.
Prediction: if you enter sunflowers and click Search, what URL do you expect the browser to request?

Try writing the markup yourself and share your attempt with your prediction.

    
14:19







/results?keyword=sunflowers







15:01






Yes—that’s the expected URL. The GET form puts the input’s name and value into the query string.

Now write the form using the hints above, then try searching for sunflowers. Share your markup and the URL you actually get.

    
15:01







I'm building a beginner Flask app for searching artworks. My /results route currently reads the keyword and returns it as text:

@app.route("/results")
def results():
keyword = request.args.get("keyword", "").strip()
return keyword

My next step is to handle empty input. If the keyword is empty or only spaces, I want to render home.html with the message "Please enter a keyword." Otherwise, keep returning the keyword for now.

Please update only this one function. Add # AI-written above it and a one-line docstring. Use simple beginner syntax and don't add other features.

Before explaining the code, ask me to predict what happens for /results?keyword=cat and /results?keyword=. Wait for my prediction.







15:04






# AI-written
@app.route("/results")
def results():
    """Takes a keyword from the URL and returns home.html or the keyword."""
    keyword = request.args.get("keyword", "").strip()
    if keyword == "":
        return render_template("home.html", message="Please enter a keyword.")
    return keyword
What do you predict happens for each URL?
- /results?keyword=cat
- /results?keyword=

    
15:04







For /results?keyword=cat, I predict the page will show "cat" because the keyword is not empty.

For /results?keyword=, I predict it will render home.html and pass the message "Please enter a keyword." Since my home.html is still empty, I think the page will be blank for now.







22:12






Both predictions are correct, including the blank page: passing message doesn’t display it unless the template uses it.

Now run both URLs. Do the results match your predictions?

    
22:12







yup







22:13






Now explain each line of the function in your own words, including the route decorator and docstring. What does each line do?

    
22:13







My Flask search form works, and my /results route handles empty input. Next, I want to use fake artwork data before connecting the API.

How do I pass a list of artwork dictionaries to results.html and display their titles, artists, and dates with a Jinja loop? Please keep it simple and help me understand how the Python variable connects to the template.







22:19






Think of it as handing a named package from Python to your template.
1. In your route, create a list named artworks. Start with two dictionaries. Give each dictionary the same keys: title, artist, and date.
2. Pass it to the template using render_template. You already passed message to home.html; use that same pattern to pass artworks to results.html.
3. In the template, write a Jinja loop. Its opening tag is {% for artwork in artworks %} and its closing tag is {% endfor %}.
4. Inside that loop, use {{ artwork["title"] }} to display the current dictionary’s title. Try the same pattern for artist and date.
The connection is the name you pass to render_template: in artworks=artworks, the left side names the template variable; the right side is your Python list. Each trip through the loop assigns one dictionary to artwork.

Try writing the list and the template call first. How would you adapt your existing call that passes message?

    
22:19







I would change the template to results.html and pass artworks instead of message:

return render_template("results.html", artworks=artworks, keyword=keyword)

The left artworks is the name used in the template, and the right artworks is the Python list. I'll use title, artist_title, and date_display as the dictionary keys so they match my HW3 API data.







22:35






Yes—your template call and explanation are correct. It also makes keyword available in the template.

Using title, artist_title, and date_display consistently will let your loop read those keys from each dictionary.

Next, write two fake artwork dictionaries and your Jinja loop. Before running it, predict: how many times will the loop run, and what will appear for each artwork?

    
22:35







With two artwork dictionaries, I predict the loop will run twice. Each time, it will show one artwork’s title, artist, and date.







22:46






Correct—the loop runs twice, displaying one artwork’s title, artist, and date each time.

Now write your two dictionaries and the template loop, then run the search. Tell me what appears, or share your attempt if you get stuck.

    
22:46