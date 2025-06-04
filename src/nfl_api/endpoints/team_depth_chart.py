# src/nfl_api/endpoints/depth_chart.py

from nfl_api.endpoints._base import Endpoint
from nfl_api.lib.domain_registry import EspnBaseDomain

class TeamDepthChart(Endpoint):
    base_domain = EspnBaseDomain.CORE 
    endpoint: str

    def __init__(self, team_id: int, season: int = 2024, **kwargs):
        self.endpoint = f"sports/football/leagues/nfl/seasons/{season}/teams/{team_id}/depthcharts"
        super().__init__(**kwargs)
