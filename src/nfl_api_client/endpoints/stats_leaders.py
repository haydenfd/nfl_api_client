# src/nfl_api/endpoints/stat_leaders.py
# Fetches top 10 in stats by category for a given season
# Stats include => passingYards, rushingYards, receivingYards, totalTackles, sacks, kickoffYards, interceptions, passingTouchdowns, quarterbackRating, rushingTouchdowns, receptions, receivingTouchdowns, totalPoints, totalTouchdowns, puntYards, passesDefended
# from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
# from nfl_api_client.endpoints._base import EndpointBase
# import re
# from nfl_api_client.lib.data import players
# from nfl_api_client.lib.parameters import TeamID

# def extract_id_from_ref(ref_url: str) -> int:
#     # Remove query string first, then extract the last path component
#     path = ref_url.split('?')[0]  # removes ?lang=en&region=us
#     return int(path.rstrip('/').split('/')[-1])

# player_dict = {p[0]: {"FIRST_NAME": p[1], "LAST_NAME": p[2], "FULL_NAME": p[3], "IS_ACTIVE": p[4]} for p in players}


# class StatsLeaders(EndpointBase):
#     def __init__(self, year: int, season_type: int = 2, limit: int = 10):
#         url = ENDPOINT_REGISTRY["STATS_LEADERS"].format(year=year, season_type=season_type, limit=limit)
#         super().__init__(url)
#         print(parse_stat_leaders_by_category(self.get_raw_json()))


# def parse_stat_leaders_by_category(response_json: dict) -> dict:
#     categories = response_json.get("categories", [])
#     parsed = {}

#     for category in categories:
#         category_name = category["name"]
#         category_display = category["displayName"]
#         leaders = []

#         for leader in category.get("leaders", []):
#             player_id = extract_id_from_ref(leader["athlete"]["$ref"])
#             team_id = extract_id_from_ref(leader["team"]["$ref"])
#             value = leader["value"]
#             display_value = leader["displayValue"]

#             player_info = player_dict.get(player_id, {
#                 "FULL_NAME": "Unknown Player",
#                 "FIRST_NAME": "",
#                 "LAST_NAME": "",
#                 "IS_ACTIVE": False
#             })

#             try:
#                 team_abbr = TeamID(team_id).name
#             except ValueError:
#                 team_abbr = f"Team {team_id}"

#             leaders.append({
#                 "PLAYER_ID": player_id,
#                 "PLAYER_NAME": player_info["FULL_NAME"],
#                 "TEAM_ID": team_id,
#                 "TEAM_ABBR": team_abbr,
#                 "VALUE": value,
#             })

#         parsed[category_name] = {
#             "displayName": category_display,
#             "leaders": leaders
#         }

#     return parsed

from typing import Optional, Dict
from nfl_api_client.endpoints._base import EndpointBase
from nfl_api_client.lib.parameters import TeamID
from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
from nfl_api_client.lib.response_parsers.stats_leaders import StatsLeadersParser


class StatsLeaders(EndpointBase):
    """
    Represents the ESPN NFL stat leaders endpoint.

    This endpoint fetches the top performers in various statistical categories for a given NFL season.

    Args:
        year (int): Season in YYYY format. 

    Example:
        ```python
        from nfl_api_client.endpoints.stat_leaders import StatLeaders

        leaders = StatLeaders(year=2024)
        passing_df = leaders.get_dataset("PASSINGYARDS").get_data_frame()
        print(passing_df.head())
        ```
    """
    def __init__(
        self,
        year: int,
        season_type: int = 2,
        limit: int = 10,
        *,
        headers: Optional[Dict[str, str]] = None,
        proxy: Optional[str] = None,
        timeout: Optional[int] = None,
    ):
        url = ENDPOINT_REGISTRY["STATS_LEADERS"].format(year=year, season_type=season_type, limit=limit)
        super().__init__(
            url,
            parser=StatsLeadersParser,
            headers=headers,
            proxy=proxy,
            timeout=timeout,
        )


if __name__ == "__main__":
    leaders = StatsLeaders(year=2024)

    passing_df = leaders.get_dataset("PUNTYARDS").get_dict()
    print(passing_df)

    passing_headers = leaders.get_dataset("PUNTYARDS").get_headers()
    print("Headers:", passing_headers)

    dataset_names = [ds.name for ds in leaders.get_data_sets()]
    print("Available datasets:", dataset_names)