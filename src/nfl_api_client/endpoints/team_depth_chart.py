# src/nfl_api/endpoints/team_depth_chart.py

from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
from nfl_api_client.endpoints._base import EndpointBase
from nfl_api_client.lib.parsers.team_depth_chart import TeamDepthChartParser

class TeamDepthChart(EndpointBase):
    def __init__(self, team_id: int, year: int):
        url = ENDPOINT_REGISTRY["TEAM_DEPTH_CHART"].format(team_id=team_id, year=year)
        super().__init__(url, parser=TeamDepthChartParser)
