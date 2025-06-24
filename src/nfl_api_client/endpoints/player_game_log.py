
from typing import Optional, Dict
from nfl_api_client.endpoints._base import BaseEndpoint
from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
from nfl_api_client.lib.response_parsers.player_game_log import PlayerGameLogParser

class PlayerGameLog(BaseEndpoint):
    def __init__(
        self,
        player_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        proxy: Optional[str] = None,
        timeout: Optional[int] = None,
    ):
        url = ENDPOINT_REGISTRY["PLAYER_GAME_LOG"].format(player_id = player_id)
        super().__init__(
            url,
            parser=PlayerGameLogParser,
            headers=headers,
            proxy=proxy,
            timeout=timeout,
        )        

# print(PlayerGameLog(3139477).get_dataset("RUSHING").get_dict())