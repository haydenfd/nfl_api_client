# import requests

# # Use this instead - https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams
# BASE_URL = "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2025/teams"
# PARAMS = {"lang": "en", "region": "us"}

# response = requests.get(BASE_URL, params=PARAMS)
# response.raise_for_status()
# data = response.json()

# total_pages = data.get("pageCount", 1)
# teams_info = []

# for page in range(1, total_pages + 1):
#     print(f"Fetching page {page} of {total_pages}")
#     page_resp = requests.get(BASE_URL, params={**PARAMS, "page": page})
#     page_resp.raise_for_status()
#     page_data = page_resp.json()

#     for item in page_data.get("items", []):
#         ref_url = item.get("$ref")
#         if not ref_url:
#             continue

#         team_resp = requests.get(ref_url)
#         team_resp.raise_for_status()
#         team = team_resp.json()

#         team_entry = {
#             "team_id": team.get("id"),
#             "team_abbreviation": team.get("abbreviation"),
#             "team_name": team.get("displayName"),
#             "team_nickname": team.get("nickname"),
#             "team_stadium": team.get("venue", {}).get("fullName", None)
#         }
#         teams_info.append(team_entry)

# for team in teams_info:
#     print(team)
# print(len(teams_info))
