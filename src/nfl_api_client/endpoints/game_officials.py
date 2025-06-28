from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
from nfl_api_client.endpoints._base import BaseEndpoint
from typing import Dict, Optional
from nfl_api_client.lib.response_parsers.game_officials import GameOfficialsParser

class GameOfficials(BaseEndpoint):
    BASE_URL = ENDPOINT_REGISTRY["GAME_OFFICIALS"]

    def __init__(
            self,
            game_id: str,
            *,
            headers: Optional[Dict[str, str]] = None,
            proxy: Optional[str] = None,
            timeout: Optional[int] = None,            
    ):
        url = self.BASE_URL.format(game_id = game_id)

        super().__init__(
            url,
            parser=GameOfficialsParser,
            headers=headers,
            proxy=proxy,
            timeout=timeout,
        )

# game_officials = GameOfficials("401671889")
# print(game_officials.get_dataset("GAME_OFFICIALS").get_dataframe())





