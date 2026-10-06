# HW1 Part 3: Decisions
# Run it:  python3 part3.py
# Your output must match expected/part3.txt exactly.

from artworks import titles, years

cutoff = 1900  # works made before this year are "old"

for i in range(len(titles)):
    if years[i] > cutoff:
        print(titles[i])

print()
old_count = 0
modern_count = 0
for i in range(len(titles)):
    if years[i] < cutoff:
        print(f"{titles[i]}: old")
        old_count = old_count + 1
    else:
        print(f"{titles[i]}: modern")
        modern_count = modern_count + 1

print()
print(f"Old: {old_count}")
print(f"Modern: {modern_count}")
