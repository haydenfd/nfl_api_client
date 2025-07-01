from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
from nfl_api_client.endpoints._base import BaseEndpoint
from typing import Dict, Optional
from nfl_api_client.lib.response_parsers.player_gamelog import PlayerGamelogParser

class PlayerGamelog(BaseEndpoint):
    BASE_URL = ENDPOINT_REGISTRY["PLAYER_GAMELOG"]

    def __init__(
            self,
            player_id: int,
            season: int = 2024,
            *,
            headers: Optional[Dict[str, str]] = None,
            proxy: Optional[str] = None,
            timeout: Optional[int] = None,    
        ):
        url = self.BASE_URL.format(player_id=player_id, season=season)

        super().__init__(
            url, 
            parser=PlayerGamelogParser,
            headers=headers,
            proxy=proxy,
            timeout=timeout,
        )

print(PlayerGamelog(player_id=3124005, season=2024).get_dataset("GAMELOG").get_dataframe().keys())
print(PlayerGamelog(player_id=3139477, season=2024).get_dataset("GAMELOG").get_dataframe().keys())
print(PlayerGamelog(player_id=3117251, season=2024).get_dataset("GAMELOG").get_dataframe().keys())
print(PlayerGamelog(player_id=4262921, season=2024).get_dataset("GAMELOG").get_dataframe().keys())