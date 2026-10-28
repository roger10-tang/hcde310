I want to do something related to golf. Are GolfCore and Open-Meteo good free APIs for a golf day planner? Can you help me check their docs, limits, and possible uses? I'll fetch the sample responses myself.







12:57






Yes—GolfCore and Open-Meteo are a useful pair for a personal or class-project golf day planner. GolfCore provides course information; Open-Meteo supplies weather. The main constraints are GolfCore’s small free allowance and Open-Meteo’s non-commercial requirement.

I checked their official documentation as of October 28, 2026, without fetching sample API responses.
	GolfCore	Open-Meteo
Main role	Find courses and inspect scorecards	Forecast conditions during a round
Free allowance	500 requests/month; 10/minute	600/minute, 5,000/hour, 10,000/day; terms also list 300,000/month
Authentication	Free API key; keyless access ends December 4, 2026	No key for free access
Commercial use	Allowed within its application-use terms	Paid access required
Attribution	Credit GolfCore and link the source course page	Credit Open-Meteo under CC BY 4.0


Sources: GolfCore keys and limits, GolfCore terms, Open-Meteo terms.

GolfCore: good for course discovery, with coverage checks.

Its documented endpoints support:
- GET /v1/courses: search by name, city, country, or nearby coordinates and radius.
- GET /v1/courses/{slug}: retrieve contact details, layouts, tees, yardages, course rating, slope, and available hole data.
Course coverage varies, and scorecards can be partial or missing. Use the returned slug rather than constructing it from a course name. The documented public endpoints do not provide live tee-time availability or booking. GolfCore API documentation

The free quota is enough for a small prototype if you cache course searches and details. Keep the key on your server. Requests stop when the free monthly allowance runs out. GolfCore permits caching for your application, but restricts redistribution, publishing datasets, and building a competing course database. Key guidance, usage terms

Open-Meteo: a strong fit for choosing when to play.

The forecast API accepts coordinates and provides seven days by default, extendable to 16. Useful fields include hourly temperature, apparent temperature, precipitation probability and amount, wind speed and gusts, plus daily sunrise, sunset, and UV index. Forecast documentation

Free access suits educational and personal projects without advertising or subscriptions. It has no uptime guarantee, and shared hosting can encounter rate limits earlier because limits apply by IP and application. Terms, pricing FAQ

A practical first version

Let someone select a course and date, then compare possible start times across an assumed four- or five-hour round. Your app could:
- Rank windows by rain probability, gusts, and temperature.
- Check whether the estimated finish precedes sunset.
- Suggest clothing or rain gear.
- Show course length and tee options alongside the forecast.
Those rankings would be your own calculations. Label recommended times as weather-based suggestions; booking availability would need another source.

When you fetch samples, check that your target courses have usable location information and scorecards, then confirm weather units, local timestamps, and missing-value behavior. I’d start with these two APIs and a small selection of courses.

  
12:58







I'll use these two. How do I get started with GolfCore and fetch data for a course near Seattle? Guide me step by step so I can make the request myself.







13:00






Start by searching near downtown Seattle, then use a returned course’s slug to request its details.
1. Create a free GolfCore API key
   Open the GolfCore developer portal, sign in, accept the API terms, and create a key. The Free plan includes 500 requests per month, up to 10 per minute.
   Copy the key when it appears—it is shown only once. Keys become required on December 4, 2026, so use one from the start. Key setup documentation
2. Open Terminal and store your key for this session
   On macOS, run:
   read -s "GOLFCORE_API_KEY?Paste your GolfCore API key: "
   Paste your key and press Return. The characters will stay hidden.
   Keep the key private and out of browser code, screenshots, and public repositories. GolfCore recommends keeping it on your server when you build the app. Key guidance
3. Search for courses within 25 miles of Seattle
   Copy this into Terminal:
   curl --get "https://api.golfcore.org/v1/courses" \
     --header "Authorization: Bearer $GOLFCORE_API_KEY" \
     --data-urlencode "near=47.6062,-122.3321" \
     --data-urlencode "radius=25" \
     --data-urlencode "limit=10" \
     --output seattle-courses.json
   This saves the response as seattle-courses.json in your current folder. near takes latitude and longitude; radius uses miles. These search parameters are documented in the Course Data API reference.
4. Read the search results
   Open the saved file in a text editor. Choose a course and copy its slug value exactly.
   Do not guess the slug from the course name—GolfCore explicitly says to take it from a search result or course page URL. Course details documentation
5. Request that course’s details
   Replace PASTE_RETURNED_SLUG_HERE below with the slug you copied:
   curl "https://api.golfcore.org/v1/courses/PASTE_RETURNED_SLUG_HERE" \
     --header "Authorization: Bearer $GOLFCORE_API_KEY" \
     --output course-details.json
   Open course-details.json. Look for the course’s contact information, layouts, tees, yardages, rating, slope, and available hole data. Some courses have incomplete scorecards; empty arrays or null values should remain marked as missing in your planner. Response field guidance
6. If a request fails, check the status
   Add --include to the request to display response headers:
   curl --include \
     "https://api.golfcore.org/v1/courses/PASTE_RETURNED_SLUG_HERE" \
     --header "Authorization: Bearer $GOLFCORE_API_KEY"
   - 401 invalid_api_key: check that you pasted an active key.
   - 429 rate_limited: wait the number of seconds in Retry-After.
   - 429 quota_exceeded: your monthly allowance is exhausted.
   Keyed responses also include monthly limit, remaining allowance, and reset headers. Error and limit reference
Once those two requests work, you’ll have the course information needed to begin connecting your planner to Open-Meteo.

  
13:00

## Additional AI assistance
Codex helped choose the APIs, explained the curl commands, organized the Resource 1 draft, and filled Resource 2 using my writing style and the saved response. I ran both API requests myself in Terminal. Codex also helped set up the folder, reviewed the submission, completed the access limits, and formatted the JSON before committing and pushing.
