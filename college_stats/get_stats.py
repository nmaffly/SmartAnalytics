# fetch a json from a url and print it
import json
import requests

response = requests.get("http://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/scoreboard")
print(response.json())

# save the json to a file in current directory
with open("./college_stats/stats2.json", "w") as f:
    json.dump(response.json(), f)