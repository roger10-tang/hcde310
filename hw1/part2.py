# HW1 Part 2: Lists and loops
# Run it:  python3 part2.py
# Your output must match expected/part2.txt exactly.

from artworks import titles

for i in range(len(titles)):
    print(f"{i + 1}. {titles[i]}")

print(f"Titles: {len(titles)}")

count = 0
longest = ""
for title in titles:
    if "a" in title.lower():
        count = count + 1
    if len(title) > len(longest):
        longest = title

print(f'Titles with an "a": {count}')
print(f"Longest: {longest}")
