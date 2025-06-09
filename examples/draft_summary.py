from nfl_api.endpoints.draft_summary import DraftSummary

# from nfl_api.lib.data import players
import re
from nfl_api.lib.parameters import TeamID

athlete_pattern = re.compile(r'/athletes/(\d+)')
team_pattern = re.compile(r'/teams/(\d+)')

TEAM_ID_TO_ABBR = {team.value: team.name for team in TeamID}

def parse_draft_summary(data):
    res = []
    for item in data.get("items", []):
        for pick in item.get("picks", []):
            athlete_ref = pick.get("athlete", {}).get("$ref", "")
            team_ref = pick.get("team", {}).get("$ref", "")
            
            match_athlete = athlete_pattern.search(athlete_ref)
            match_team = team_pattern.search(team_ref)

            player_id = int(match_athlete.group(1)) if match_athlete else None
            team_id = int(match_team.group(1)) if match_team else None
            team_abbr = TEAM_ID_TO_ABBR.get(team_id)

            res.append({
                "pick": pick.get("pick"),
                "round": pick.get("round"),
                "overall_pick": pick.get("overall"),
                "player_id": player_id,
                "team_id": team_id,
                "team_abbreviation": team_abbr,
                "traded": pick.get("traded", False),
                "trade_notes": pick.get("tradeNote", "")
            })
    return res

def main():
    depth_chart = DraftSummary()
    data = depth_chart.get_dict()
    print(parse_draft_summary(data)[0:15])


if __name__ == "__main__":
    main()