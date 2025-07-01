from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
from nfl_api_client.endpoints._base import BaseEndpoint
from typing import Dict, Optional
from nfl_api_client.lib.response_parsers.game_scoring_plays import GameScoringPlaysParser

class GameScoringPlays(BaseEndpoint):
    BASE_URL = ENDPOINT_REGISTRY["GAME_SUMMARY"]

    def __init__(
            self,
            game_id: int,
            *,
            headers: Optional[Dict[str, str]] = None,
            proxy: Optional[str] = None,
            timeout: Optional[int] = None,    
    ):
        url = self.BASE_URL.format(game_id=game_id)

        super().__init__(
            url,
            parser=GameScoringPlaysParser,
            headers=headers,
            proxy=proxy,
            timeout=timeout,
        )

# print(GameScoringPlays(game_id=401671889).get_dataset("SCORING_PLAYS").get_dataframe())