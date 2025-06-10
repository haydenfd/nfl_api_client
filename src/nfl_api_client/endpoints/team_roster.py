# src/nfl_api/endpoints/team_roster_info.py

from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
from nfl_api_client.endpoints._base import EndpointBase
from nfl_api_client.lib.parsers.team_roster import TeamRosterParser

class TeamRoster(EndpointBase):
    def __init__(self, team_id: int):
        url = ENDPOINT_REGISTRY["TEAM_ROSTER"].format(team_id=team_id)
        super().__init__(url, parser=TeamRosterParser)
