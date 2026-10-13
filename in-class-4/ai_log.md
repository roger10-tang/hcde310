Me:

I'm a Human Centered Design & Engineering student learning Python so I can prototype interactive apps. I'm a beginner. Please act as my tutor.

Rules:

- Never write code for my assignment, even if I ask. If I ask, remind me of this rule and give me a hint instead.
- You may show a tiny example (3 lines or fewer) that uses different data and a different task from mine.
- Ask me one guiding question at a time, and wait for my answer.
- When I paste an error, explain in plain language what kind of error it is and what it usually means. Ask me which line I think it points to before you tell me.

My routine is Try → Predict → Run → Explain → Log. Help me follow it:

- If I haven't shown you my attempt, ask for it first.
- Before you explain what some code does, ask me to predict what it will print.
- After you explain something, ask me to explain it back in my own words, and tell me what I got right and what I missed.

My question is about Snippet 5 from In-class 4. This is the original code:

```python
def longest_title(titles):
    """Return the longest title in a list of titles."""
    longest = ""
    for t in titles:
        if len(t) > len(longest):
            longest = t
    print(longest)

title = longest_title(["Nighthawks", "The Bedroom", "Water Lilies"])
print(title.upper())
```

My guess before asking: there should be a "return" according to the structure? change print to return.
I expected it to print the longest title in uppercase.
The error from the AI's run of the original code was:
AttributeError: 'NoneType' object has no attribute 'upper'

I already received a direct fix from another AI chat: it changed print to return and the final check passed. I want to understand why, rather than receive the solution again. Please give me one guiding question and wait for my answer. Don't edit or run my assignment files.

17:00

AI:

This is an **AttributeError**: Python tried to use an operation that the value doesn’t support. Here, the error says the value was `None`, which has no `.upper()` method.

Which line in the original code do you think the error points to?

17:00

Me:

I think line 41, `print(title.upper())`, because title is None. I'm still not sure why printing longest doesn't give title a value.

17:04

AI:

You got that right: `title` is `None`, so calling `.upper()` on it causes the error.

`print(longest)` displays a value on the screen. `return` sends a value back to the place that called the function. When a function finishes without a `return`, Python sends back `None`, which is what gets assigned to `title`.

In your own words, how is displaying a value different from sending it back to the caller?

17:04

Me:

print just shows the value on screen. return gives it back so title can save it and use .upper(). without return, title is None.

17:05

AI:

Exactly—you got all three points right, and nothing essential is missing. More precisely, a function that finishes without `return` returns `None`.

For your **Log** step, what one-sentence reminder would you write to help yourself distinguish `print` from `return` next time?

17:05
