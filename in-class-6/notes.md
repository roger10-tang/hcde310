# In-class 6 notes

## What happens with a wrong key? What status code?

##the API returns 403. The program prints "Request failed."

## Where does your key live, and why isn't it in earth.py?

##key is in .env in the in-class-6 folder. load_dotenv() reads the file,
and os.getenv("NASA_API_KEY") gets the key. The code goes on GitHub, so the
key should not be in earth.py. .gitignore keeps .env out of Git

## Stuck? Where?

##The code returned 200 with the valid key and printed the first photo's
caption and date. It returned 403 with a wrong key.
