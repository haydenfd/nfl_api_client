# src/nfl_api/endpoints/draft_summary.py

# Fetches draft info (player, team drafted to, pick, round, trade notes) for a given year
# endpoint => http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{YYYY}/draft/rounds

# SOME PLAYERS BIO INFO MIGHT BE OUTDATED. THIS COMES FROM ESPN. 

import httpx
import asyncio 
from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
# import json
from nfl_api_client.lib.utils import extract_team_id_from_ref
from nfl_api_client.lib.parameters import TeamID
import re
from typing import Optional
import pandas as pd

def extract_draft_id_from_ref(ref: str) -> Optional[int]:
    match = re.search(r'/athletes/(\d+)', ref)
    return int(match.group(1)) if match else None

class DraftSummary:
    BASE_URL = ENDPOINT_REGISTRY["DRAFT_SUMMARY"]

    def __init__(self, year: int = 2025):
        self.url = self.BASE_URL.format(year=year)
        self.data = None

    async def _fetch(self):
        async with httpx.AsyncClient() as client:
                response = await client.get(self.url)
                response.raise_for_status()
                self.data = response.json()
    async def _fetch_player_info(self, client, draft_id, url):
        try:
            resp = await client.get(url)
            resp.raise_for_status()
            data = resp.json()
            return {
                "draft_id": draft_id,
                "player_first_name": data.get("firstName"),
                "player_last_name": data.get("lastName"),
                "player_name": data.get("fullName"),
                "weight": data.get("weight"),
                "height": data.get("height"),
                "position": data.get("position", {}).get("displayName", ""),
                "player_id": extract_draft_id_from_ref(data.get("athlete", {}).get("$ref", ""))
            }
        except Exception:
            return {
                "draft_id": draft_id,
                "player_first_name": None,
                "player_last_name": None,
                "player_name": None,
                "weight": None,
                "height": None,
            }

    async def _process(self):
        all_picks = []
        athlete_ref_map = {}

        rounds = self.data.get("items", [])
        for rd in rounds:
            for pick in rd.get("picks", []):
                athlete_ref = pick.get("athlete", {}).get("$ref", "")
                draft_id = extract_draft_id_from_ref(athlete_ref)
                team_ref = pick.get("team", {}).get("$ref", "")
                traded = pick.get("traded", False)
                trade_note = pick.get("tradeNote") if traded else None

                if draft_id and athlete_ref:
                    athlete_ref_map[draft_id] = athlete_ref

                all_picks.append({
                    "round_pick": pick.get("pick"),
                    "round": pick.get("round"),
                    "overall_pick": pick.get("overall"),
                    "team_abbr": TeamID(extract_team_id_from_ref(team_ref)).name if team_ref else None,
                    "draft_id": draft_id,
                    "traded": traded,
                    "trade_note": trade_note
                })

        # Concurrently fetch all athlete profiles
        async with httpx.AsyncClient() as client:
            tasks = [
                self._fetch_player_info(client, draft_id, url)
                for draft_id, url in athlete_ref_map.items()
            ]
            player_info = await asyncio.gather(*tasks)

        player_info_map = {entry["draft_id"]: entry for entry in player_info}

        # Merge player info into all_picks
        for pick in all_picks:
            info = player_info_map.get(pick["draft_id"], {})
            pick.update(info)
        return pd.DataFrame(all_picks)
             

if __name__ == "__main__":
    
    async def main():
        draft = DraftSummary(2025)
        await draft._fetch()
        res = await draft._process()
        print(res[res["weight"] == 0.0])

    asyncio.run(main())
     