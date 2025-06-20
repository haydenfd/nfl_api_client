from typing import Optional, Union, Dict
from nfl_api_client.endpoints._base import BaseEndpoint
from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
from nfl_api_client.lib.parameters import SeasonTypeID
from nfl_api_client.lib.response_parsers.player_career_stats import PlayerCareerStatsParser

class PlayerCareerStats(BaseEndpoint):
    """
    Endpoint for fetching a player's career statistics across all seasons and categories (passing, rushing, etc).

    Only categories relevant to the player's position will be returned. For example, a quarterback may have
    passing and rushing stats, while a kicker may only have scoring.

    Args:
        player_id (int): The ESPN player ID.
        season_type (int or SeasonType, optional): Defaults to 2 (regular season).

    Example:
        ```python
        from nfl_api_client.endpoints.player_career_stats import PlayerCareerStats

        justin_jefferson_stats = PlayerCareerStats(player_id=4262921)
        df = justin_jefferson_stats.get_dataset("RECEIVING").get_data_frame()
        print(df.head())        
        ```
    """

    def __init__(
        self,
        player_id: int,
        season_type: Union[int, SeasonTypeID] = SeasonTypeID.REG,
        *,
        headers: Optional[Dict[str, str]] = None,
        proxy: Optional[str] = None,
        timeout: Optional[int] = None,
    ):
        if isinstance(season_type, SeasonTypeID):
            season_type = season_type.value

        url = ENDPOINT_REGISTRY["PLAYER_CAREER_BASIC_STATS"].format(
            player_id=player_id,
            season_type=season_type,
        )
        super().__init__(
            url=url,
            parser=PlayerCareerStatsParser,
            headers=headers,
            proxy=proxy,
            timeout=timeout,
        )

player = PlayerCareerStats(player_id=4262921)
df = player.get_dataset("SCORING").get_data_frame()
print(df)