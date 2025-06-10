# src/nfl_api/endpoints/draft_summary.py

# Fetches draft info (player, team drafted to, pick, round, trade notes) for a given year
# endpoint => http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{YYYY}/draft/rounds

from nfl_api_client.endpoints._base import Endpoint
from nfl_api_client.lib.endpoint_registry import EspnBaseDomain

class DraftSummary(Endpoint):

    base_domain = EspnBaseDomain.CORE 
    endpoint: str

    def __init__(self, season: int = 2025, **kwargs):
        self.endpoint = f"sports/football/leagues/nfl/seasons/{season}/draft/rounds"
        super().__init__(**kwargs)
