import requests 
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/tuvvshe"
req = requests.get(github_profile)
scraper = bs(req.content, "html.praser")
profile_picture = scraper.find("img", {"alt": "Avatar"}) ["src"]
print(profile_picture)