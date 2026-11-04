import os
import requests
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GOLFCORE_API_KEY")
url = "https://api.golfcore.org/v1/courses/pebble-beach"
headers = {"User-Agent": "HCDE310 R1 course guide"}
if key is not None and key != "":
    headers["Authorization"] = f"Bearer {key}"

try:
    response = requests.get(url, headers=headers, timeout=10)
except requests.RequestException:
    response = None

if response is None:
    print("Request failed. Check your connection and try again.")
elif response.status_code != 200:
    print("Request failed:", response.status_code)
    print("Check the course slug, API key, or request allowance.")
else:
    data = response.json()
    print(data.get("name") or "Name unavailable")
    city = data.get("city") or "Unknown"
    region = data.get("region") or "Unknown"
    print(f"Location: {city}, {region}")
    print("Holes:", data.get("hole_count"))
    print("Par:", data.get("par_total"))
    print("Year built:", data.get("year_built") or "Unavailable")
    for layout in data.get("layouts") or []:
        print("Layout:", layout.get("name") or "Unnamed")
        for tee in layout.get("tees") or []:
            name = tee.get("name") or "Unnamed"
            gender = tee.get("gender") or "Unavailable"
            yards = tee.get("yards")
            if yards is None:
                yards = "Unavailable"
            print(f"  Tee: {name} | Rating category: {gender} | {yards} yards")
    print("Source: GolfCore", data.get("url") or "https://www.golfcore.org/")
