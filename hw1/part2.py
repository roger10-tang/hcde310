from artworks import titles

number = 1
for title in titles:
    print(f"{number}. {title}")
    number = number + 1

total = len(titles)
print(f"Titles: {total}")

count = 0
for title in titles:
    lowercase_title = title.lower()
    if "a" in lowercase_title:
        count = count + 1
print(f'Titles with an "a": {count}')

longest = titles[0]
for title in titles:
    title_length = len(title)
    longest_length = len(longest)
    if title_length > longest_length:
        longest = title
print(f"Longest: {longest}")
