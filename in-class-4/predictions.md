# Class 4: Five broken snippets

Your name: roger tang
Collaborator: won kim

# Part 1: Predict

**Don't run anything yet.** Read each snippet in `exercise.py` and write your guesses. A wrong guess is fine: the point is to compare.

## Snippet 1
- Which line breaks? 8th line: exhibit["Room"] is capital letter
- What error will Python show? (the kind and the message) keyerror
- What's the fix? change "R" to "r"

## Snippet 2
- Which line breaks? 12th: string can't add integer directly 
- What error will Python show? (the kind and the message) typeerror
- What's the fix? use "," to replace "+"

## Snippet 3
- Which line breaks? 17th, i + 1 is over the maximum of the list range
- What error will Python show? (the kind and the message) indexerror
- What's the fix? for i in range(len(exhibits)):

## Snippet 4
- Which line breaks? 29, visit doesn't have "s"
- What error will Python show? (the kind and the message) nameerror
- What's the fix? change the name to "visits"

## Snippet 5
- Which line breaks? there should be a "return" according to the structure?
- What error will Python show? (the kind and the message) typeerror
- What's the fix? change print to return

# Part 2: Run

Run `python3 exercise.py`. Python stops at the first error, so fix that snippet in `exercise.py`, run again, and see the next one. Fill in what actually happened.

## Snippet 1
- Which line broke? 8th line: Room is capital letter
- What error did Python show? KeyError: 'Room'; after changing R to r: TypeError: can only concatenate str (not "int") to str
- What's the fix? change "R" to "r", also change "+" to ","

## Snippet 2
- Which line broke? 12th: string can't add integer
- What error did Python show? TypeError: can only concatenate str (not "int") to str
- What's the fix? use "," to replace "+"

## Snippet 3
- Which line broke? 17th, range is too big
- What error did Python show? IndexError: list index out of range
- What's the fix? remove + 1 in range

## Snippet 4
- Which line broke? 29, visit doesn't have "s"
- What error did Python show? NameError: name 'visit' is not defined. Did you mean: 'visits'?
- What's the fix? change to "visits"

## Snippet 5
- Which line broke? 41, title is None
- What error did Python show? AttributeError: 'NoneType' object has no attribute 'upper'
- What's the fix? change print to return

When all five are fixed, run `python3 check.py` until it says ✓.

Bonus: Snippet 5 prints something *before* it crashes. What, and why does it still crash?

# Part 3: Tutor practice (one snippet)

Pick one snippet. Write your guess first, then ask your tutor. Paste the chat (or a share link) below.

- Snippet #: 5
- Our guess before asking: there should be a "return" according to the structure? change print to return
- Chat: [ai_log.md](ai_log.md)
- Did it give you too much? What did you do? yes it gave the fix directly. I asked it to change the code based on my guesses, and the check passed. I explained print and return to my partner
