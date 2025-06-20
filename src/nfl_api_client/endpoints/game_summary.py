from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
import httpx
import asyncio
import json
import pandas as pd

class GameSummary:
    BASE_URL = ENDPOINT_REGISTRY["GAME_SUMMARY"]

    def __init__(self, game_id: int):
        self.url = self.BASE_URL.format(game_id=game_id)
        self.data = None
        self.result_sets = {}
        
    async def fetch(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(self.url)
            response.raise_for_status()
            self.data = response.json()
        return self.data

    def process(self):
        boxscore_field = self.data.get("boxscore", {})
        teams_field = boxscore_field.get("teams", [])

        for team in teams_field:
            team_info = team.get("team", {})
            team_name = team_info.get("name", "")
            team_id = team_info.get("id", "")
            team_code = team_info.get("abbreviation", "")

            home_away = team.get("homeAway", "")
            team_key = "homeTeam" if home_away == "home" else "awayTeam"

            # Process stats
            stats = {}
            for stat in team.get("statistics", []):
                stat_name = stat.get("name", "")
                stat_val = stat.get("displayValue", None)
                stats[stat_name] = stat_val

            self.result_sets[team_key] = {
                "team_name": team_name,
                "team_id": team_id,
                "team_code": team_code,
                "stats": stats
            }

        def get_scoring_plays():
            self.result_sets["scoring_plays"] = []
            scoring_plays = self.data.get("scoringPlays", [])
            for play in scoring_plays:
                play_data_entry = {
                    "type_abbreviation": play.get("type", {}).get("abbreviation", ""),
                    "type_description": play.get("type", {}).get("text", ""),
                    "play_description": play.get("text", ""),
                    "away_score": play.get("awayScore"),
                    "home_score": play.get("homeScore"),
                    "period": play.get("period", {}).get("number"),
                    "clock": play.get("clock", {}).get("displayValue"),
                    "team_code": play.get("team", {}).get("abbreviation",""),
                    "team_name":play.get("team", {}).get("displayName", ""), 
                }

                self.result_sets["scoring_plays"].append(play_data_entry)
        get_scoring_plays()
        print(pd.DataFrame(self.result_sets["scoring_plays"]))

# Usage
if __name__ == "__main__":
    async def main():
        summary = GameSummary(401671819)
        data = await summary.fetch()
        summary.process()


    asyncio.run(main())