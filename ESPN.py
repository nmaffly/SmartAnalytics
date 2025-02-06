import requests

TEAM_ID = 302  # UC Davis ID from ESPN

url = f"https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/teams/{TEAM_ID}"
response = requests.get(url)

if response.status_code == 200:
    team_data = response.json()
    #print(team_data)  
else:
    print(f"Failed to fetch data: {response.status_code}")


team_info = team_data["team"]
team_name = team_info["displayName"]
team_abbreviation = team_info["abbreviation"]
team_logo = team_info["logos"][0]["href"]
standing_summary = team_info.get("standingSummary", "N/A")

print(f"Team: {team_name} ({team_abbreviation})")
print(f"Standing: {standing_summary}")
print(f"Logo URL: {team_logo}")

overall_record = next(record for record in team_info["record"]["items"] if record["type"] == "total")

wins = next(stat["value"] for stat in overall_record["stats"] if stat["name"] == "wins")
losses = next(stat["value"] for stat in overall_record["stats"] if stat["name"] == "losses")
avg_points_for = next(stat["value"] for stat in overall_record["stats"] if stat["name"] == "avgPointsFor")
avg_points_against = next(stat["value"] for stat in overall_record["stats"] if stat["name"] == "avgPointsAgainst")

print(f"Overall Record: {int(wins)}-{int(losses)}")
print(f"Avg Points For: {avg_points_for}")
print(f"Avg Points Against: {avg_points_against}")

home_record = next(record for record in team_info["record"]["items"] if record["type"] == "home")
away_record = next(record for record in team_info["record"]["items"] if record["type"] == "road")

home_wins = next(stat["value"] for stat in home_record["stats"] if stat["name"] == "wins")
home_losses = next(stat["value"] for stat in home_record["stats"] if stat["name"] == "losses")
away_wins = next(stat["value"] for stat in away_record["stats"] if stat["name"] == "wins")
away_losses = next(stat["value"] for stat in away_record["stats"] if stat["name"] == "losses")

print(f"Home Record: {int(home_wins)}-{int(home_losses)}")
print(f"Away Record: {int(away_wins)}-{int(away_losses)}")

next_game = team_info.get("nextEvent", [{}])[0]
if next_game:
    opponent = next_game["competitions"][0]["competitors"][0]["team"]["displayName"]
    game_date = next_game["date"]
    game_location = next_game["competitions"][0]["venue"]["fullName"]
    opponent_logo = next_game["competitions"][0]["competitors"][0]["team"]["logos"][0]["href"]

    print(f"Next Game: UC Davis vs {opponent}")
    print(f"Date: {game_date}")
    print(f"Location: {game_location}")
    print(f"Opponent Logo: {opponent_logo}")
else:
    print("No upcoming games found.")



