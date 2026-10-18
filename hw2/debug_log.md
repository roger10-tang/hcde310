# HW2 Part 5 – Debug log (`debug_log.md`)

Record **at least 2 errors** you hit. No errors? Break something on purpose and log it. For each error, write:

---

## Entry 1

### 1. Error message
*copy it exactly*
/Library/Frameworks/Python.framework/Versions/3.14/Resources/Python.app/Contents/MacOS/Python: can't open file '/Users/roger/Documents/hcde310/check.py': [Errno 2] No such file or directory

### 2. What I thought it meant
I thought I had typed something wrong because Python could not find the file

### 3. What it actually meant
I was running the command from the hcde310 folder, but check.py was inside hw2 Python was looking in the wrong folder

### 4. The fix
I entered cd /Users/roger/Documents/hcde310/hw2 and ran python3 check.py again. The checker started successfully

## Entry 2

### 1. Error message
*copy it exactly*
File "/Users/roger/Documents/hcde310/hw2/part4.py", line 17
    titles = []
IndentationError: unexpected indent

### 2. What I thought it meant
I wasn't sure, but I thought there was a spacing error

### 3. What it actually meant
The indentation inside works_by was inconsistent. Some lines had three leading spaces while others at the same level had four. Python uses indentation to identify code blocks

### 4. The fix
AI guide me to fix