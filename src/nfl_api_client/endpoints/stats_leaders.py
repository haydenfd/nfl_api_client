# Fetches top 10 in stats by category for a given season
# Stats include => passingYards, rushingYards, receivingYards, totalTackles, sacks, kickoffYards, interceptions, passingTouchdowns, quarterbackRating, rushingTouchdowns, receptions, receivingTouchdowns, totalPoints, totalTouchdowns, puntYards, passesDefended

from typing import Optional, Dict
from nfl_api_client.endpoints._base import BaseEndpoint
from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
from nfl_api_client.lib.response_parsers.stats_leaders import StatsLeadersParser

class StatsLeaders(BaseEndpoint):
    """
    Represents the ESPN NFL stat leaders endpoint.

    This endpoint fetches the top performers in various statistical categories for a given NFL season.

    Args:
        year (int): Season in YYYY format. 

    Example:
        ```python
        from nfl_api_client.endpoints.stats_leaders import StatsLeaders

        leaders = StatsLeaders(year=2024)
        passing_df = leaders.get_dataset("PASSINGYARDS").get_dataframe()
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


# if __name__ == "__main__":
#     leaders = StatsLeaders(year=2024)

#     passing_df = leaders.get_dataset("PUNT_YARDS").get_dict()
#     print(passing_df)

    # passing_headers = leaders.get_dataset("PUNTYARDS").get_headers()
    # print("Headers:", passing_headers)

    # dataset_names = [ds.name for ds in leaders.get_data_sets()]
    # print("Available datasets:", len(dataset_names))