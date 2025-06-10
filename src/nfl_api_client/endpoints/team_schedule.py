# src/nfl_api/endpoints/team_schedule.py

from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
from nfl_api_client.endpoints._base import EndpointBase
from nfl_api_client.lib.parsers.team_schedule_parser import TeamScheduleParser

class TeamSchedule(EndpointBase):

    BASE_URL = ENDPOINT_REGISTRY["TEAM_SCHEDULE"]

    def __init__(self, team_id: int, year: int):
        url = self.BASE_URL.format(team_id=team_id) + f"?season={year}"
        super().__init__(url=url, parser=TeamScheduleParser)