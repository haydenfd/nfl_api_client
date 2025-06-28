from typing import Dict, Optional
from nfl_api_client.endpoints._base import BaseEndpoint
from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
from nfl_api_client.lib.response_parsers.season_standings import (
    SeasonStandingsConferenceParser,
    SeasonStandingsDivisionParser,
    SeasonStandingsLeagueParser,
)

ALLOWED_GROUPS = {
    "league",
    "conference",
    "division",
}

class SeasonStandings(BaseEndpoint):
    BASE_URL = ENDPOINT_REGISTRY["SEASON_STANDINGS"]

    def __init__(
            self, 
            season: int = 2024,
            group: str = "league",
            *,
            headers: Optional[Dict[str, str]] = None,
            proxy: Optional[str] = None,
            timeout: Optional[int] = None,                
        ):

        self.data = None
        self.view = "standings"
        if group not in ALLOWED_GROUPS:
            raise ValueError(
                f"Invalid group '{group}'. Must be one of: {', '.join(ALLOWED_GROUPS)}"
            )
        url = self.BASE_URL.format(season=season, view=self.view, group = group)
        self.parser = None

        if group == "division":
            self.parser = SeasonStandingsDivisionParser
        elif group == "conference":
            self.parser = SeasonStandingsConferenceParser
        else:
            self.parser = SeasonStandingsLeagueParser
        super().__init__(
            url=url,
            parser=self.parser,
            headers=headers,
            proxy=proxy,
            timeout=timeout,
        )
