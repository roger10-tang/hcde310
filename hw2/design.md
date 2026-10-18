# HW2 Part 1 – Model first (in `design.md`, no code)

---

## 1. Why is `artworks` a list of dictionaries and not one big dictionary? What would you lose or gain the other way?

## A big dictionary will cause the keys to repeat like "title" causing error. Using unique IDs as keys would make lookup easier, but manage could be harder.

## 2. Which fields are sometimes missing? What should the app show when they are?

## Some artworks are missing "artist", "year", "medium". It should show "Unknown" for missing

