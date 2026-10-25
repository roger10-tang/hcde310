# HW3 Part 4 – Save the results

AI Use: Stage 3 (Little helper)

Write a new function, `save_results(artworks, filename)`, that writes one line per artwork (title, artist, date) to a `.txt` file. Call it so every search saves its results. Then run `fetch.py` for real once, with a search you pick, and **commit the `.txt` file it made**: that's your proof the live call works.

You may have the AI write this function (about 10 lines) using the **[Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt)** (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in `ai_log.md` **as you go**:

Done early? Add `sort_by_date(artworks)` too (not graded).

---

## 1. Try
*paste your own attempt or plan for the function, even if it doesn't work*
open a text file using the given filename, loop through the artworks, 
and write each artwork's title, artist, and date on a separate line. 
If information is missing, I‘ll just use a default value.

## 2. Chat (AI only)

AI helped with the plan, notes, code, debugging, and prediction. The plan above was based on an AI example.

*paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."*
params = {"term" = 'q'}







14:46






You’ve got the braces and two parts in place. A dictionary uses a colon : between a key and its value. Here, "q" is the key, and term is the variable supplying the value—so the variable needs no quotes.

How would you revise your attempt using those hints?

  
14:46







params = {"term" : 'q'}







14:47






You fixed the separator—the colon is right. The key and value are still reversed, and quoting term makes it literal text instead of a variable.

Which belongs before the colon: the key "q" or the variable term?

  
14:47







params = {"q" : 'term'}







14:47






You’ve placed "q" correctly as the key, and the colon is right. One detail remains: 'term' means the literal text “term,” while term uses the value stored in the variable.

What would you change so Python uses the variable’s value?

  
14:47







"q": term, "fields": FIELDS







14:49






You’ve correctly paired both keys with their variables, and the comma separates the pairs.

What would you add around those pairs, and before them, to store the complete dictionary in params?

  
14:49







I'm trying to understand if not artworks:. I know artworks is a list, but why does adding not check whether it is empty? Could you explain with a tiny example using different data, without writing my assignment code?







14:56






Let’s predict first with a tiny example:
snacks = []
print(bool(snacks))
print(not snacks)
bool() shows whether Python treats a value as true or false. What do you predict the two lines will print?

  
14:56







false,true







14:56






Correct! Python prints them as False and True.

An empty list counts as false in a condition. not flips that to true, so if not artworks: runs its indented block when artworks is empty. A list with any items counts as true, so not makes it false.

In your own words, why does not artworks become true when the list is empty?

  
14:56







cuz it's empty, means no data to print







14:57






You’re right that it’s empty—there are no items. The missing piece is that Python treats an empty list as False, and not flips that to True. This check works whether or not you plan to print anything.

If artworks contained one item, would not artworks be True or False?

  
14:57







false







14:57






Correct—False. A list with one item counts as true, and not flips it to false.

For your Log step, how would you summarize what if not artworks: checks in one sentence?

  
I'm a Human Centered Design & Engineering student learning Python so I can prototype interactive apps. I follow a routine: Try → Predict → Run → Explain → Log.
My attempt so far: [paste your code or plan, even if it doesn't work] **Where I'm stuck:** [one sentence] **The function I need:** `[name]([inputs])` takes [what] and returns [what].
Rules: - Write only this one function, about 10 lines or fewer. No other code, and don't change mine. - Put # AI-written on the line above the function. - Start the function with a one-line docstring that says what it takes and returns. - Use only what a beginner would know: loops, if, lists, dictionaries, and the libraries I'm already using. If you need something new, tell me its name and what it does in one line. - Don't explain the code yet. Ask me to predict what it returns for [one real input]. Wait for my prediction. - After I've run it and told you the result, ask me to explain each line in my own words. Correct anything I got wrong, then ask me about one line I skipped. - Then suggest one small change I could make myself (don't write it). Wait until I tell you what I changed. - Then ask me: what's one thing that surprised you? Don't answer it for me. - For anything other than this one function, act as my tutor: hints and questions, no code.







13:46






Please fill in these three details so we can start:
- My attempt so far: your code or plan.
- Where I’m stuck: one sentence.
- The function I need: its name, inputs, and what it should return.

  
13:46







My attempt so far:
My plan is to open a text file using the given filename, loop through the artworks, and write each artwork's title, artist, and date on a separate line. If information is missing, I'll use a default value.
Where I'm stuck:
I don't know how to open a file and write each artwork's information to it in Python.
The function I need:
save_results(artworks, filename) takes a list of artwork dictionaries and a filename. It writes each artwork's title, artist, and date on a separate line in a text file and returns None.







15:06






with open(..., "w") opens a file for writing and closes it afterward; .get() supplies defaults for missing keys; an f-string inserts values into text.
# AI-written
def save_results(artworks, filename):
    """Take artwork dictionaries and a filename, write one artwork per line, and return None."""
    with open(filename, "w", encoding="utf-8") as file:
        for artwork in artworks:
            title = artwork.get("title", "Unknown title")
            artist = artwork.get("artist", "Unknown artist")
            date = artwork.get("date", "Unknown date")
            file.write(f"{title}, {artist}, {date}\n")
Before running it, predict: with artworks = [{"title": "Water Lilies", "artist": "Claude Monet"}] and filename = "artworks.txt", what will the function return, and what will the file contain?

  
15:06







My API uses "artist_title" and "date_display", rather than "artist" and "date". Some values can also be null, which becomes None in Python. Please revise only this function to use those field names and handle both missing keys and None values. Then ask me to predict the file contents using actual sample data before I run it.







15:07






# AI-written
def save_results(artworks, filename):
    """Take artwork dictionaries and a filename, write one artwork per line, and return None."""
    with open(filename, "w", encoding="utf-8") as file:
        for artwork in artworks:
            title = artwork.get("title") or "Unknown title"
            artist = artwork.get("artist_title") or "Unknown artist"
            date = artwork.get("date_display") or "Unknown date"
            file.write(f"{title}, {artist}, {date}\n")
Before running it, what exact file contents do you predict for this sample input?

[{"title": "Water Lilies", "artist_title": "Claude Monet", "date_display": None}, {"title": None, "date_display": "1906"}]

  
15:07







Water Lilies, Claude Monet, Unknown date
Unknown title, Unknown artist, 1906







15:08






That’s my prediction too. Run the function with that sample input, then tell me what the file contains and whether it matches your prediction.

  


## 3. Predict, then compare
*before you run the function, write what you think the file will contain for the sample data (`check.py` uses it) or for your search. Then paste what it actually contains. (A wrong prediction gets full credit. Don't edit it after running.)*


Prediction discussed in the AI chat before running (AI-assisted; added to this file afterward):

```text
Water Lilies, Claude Monet, Unknown date
Unknown title, Unknown artist, 1906
```

Actual result (`prediction_test.txt`):

```text
Water Lilies, Claude Monet, Unknown date
Unknown title, Unknown artist, 1906
```

The actual result matched the prediction.

## 4. What surprised me
*one or two sentences. Where were you wrong, or what did you learn? For example: "I thought a missing artist would print `none`, but `.get` gave the fallback `unknown`."*
I learned that a missing key and a value of None are different. Using `or` lets the program use a default value in both cases

## 5. Change one thing yourself
*once the function works, change one thing about it by hand, no AI. For example: a different line format (date first), a filename based on the search term, or sorted lines. Write what you changed and why, in one or two sentences.*
I changed the output order from title, artist, date to date, title, artist just because it makes the date easier to find and an easy change
