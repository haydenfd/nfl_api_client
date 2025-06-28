from typing import Optional, Dict
from nfl_api_client.endpoints._base import BaseEndpoint
from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
from nfl_api_client.lib.parameters import SeasonTypeID
from nfl_api_client.lib.response_parsers.player_career_stats import PlayerCareerStatsParser

class PlayerCareerStats(BaseEndpoint):

    def __init__(
        self,
        player_id: int,
        season_type: SeasonTypeID = 2,
        *,
        headers: Optional[Dict[str, str]] = None,
        proxy: Optional[str] = None,
        timeout: Optional[int] = None,
    ):
        url = ENDPOINT_REGISTRY["PLAYER_CAREER_BASIC_STATS"].format(player_id = player_id, season_type = season_type)
        super().__init__(
            url,
            parser=PlayerCareerStatsParser,
            headers=headers,
            proxy=proxy,
            timeout=timeout,
        )



# josh_allen = PlayerCareerStats(player_id=3918298)
# print(josh_allen.get_dataset("PASSING").get_dataframe())
