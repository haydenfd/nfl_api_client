from typing import Dict, Optional
from nfl_api_client.endpoints._base import BaseEndpoint
from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
from nfl_api_client.lib.response_parsers.season_standings_playoffs import (
    SeasonStandingsPlayoffsParser
)


class SeasonStandingsPlayoffs(BaseEndpoint):
    BASE_URL = ENDPOINT_REGISTRY["SEASON_STANDINGS"]

    def __init__(
            self, 
            season: int = 2024,
            *,
            headers: Optional[Dict[str, str]] = None,
            proxy: Optional[str] = None,
            timeout: Optional[int] = None,                
        ):

        self.data = None
        self.view = "playoff"
        url = self.BASE_URL.format(season=season, view=self.view, group = "conference")
        self.parser = SeasonStandingsPlayoffsParser

        super().__init__(
            url=url,
            parser=self.parser,
            headers=headers,
            proxy=proxy,
            timeout=timeout,
        )


if __name__ == "__main__":
    standings = SeasonStandingsPlayoffs(season=2024)
    print(standings.get_dataset("AFC").get_data_frame())
