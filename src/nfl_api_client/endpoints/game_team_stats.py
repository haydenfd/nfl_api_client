from nfl_api_client.endpoints._base import BaseEndpoint
from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
from typing import Optional, Dict
from nfl_api_client.lib.response_parsers.game_team_stats import GameTeamStatsParser

class GameTeamStats(BaseEndpoint):
    BASE_URL = ENDPOINT_REGISTRY["GAME_SUMMARY"]
    
    def __init__(
        self,
        game_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        proxy: Optional[str] = None,
        timeout: Optional[int] = None,            
        ):
        self.url = self.BASE_URL.format(game_id = game_id)
        super().__init__(
            self.url,
            parser=GameTeamStatsParser,
            headers=headers,
            proxy=proxy,
            timeout=timeout,
        )        

# plays = GameTeamStats(401326315)
# print(plays.get_dataset("TEAM_STATS").get_dataframe())
