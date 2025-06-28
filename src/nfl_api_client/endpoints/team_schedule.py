from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
from nfl_api_client.endpoints._base import BaseEndpoint
from nfl_api_client.lib.response_parsers.team_schedule import TeamScheduleParser
from nfl_api_client.lib.parameters import TeamID
from typing import Union, Optional, Dict

class TeamSchedule(BaseEndpoint):
   
    BASE_URL = ENDPOINT_REGISTRY["TEAM_SCHEDULE"]

    def __init__(
            self, 
            team_id: Union[int, TeamID], 
            season: int = 2025,
            *,
            headers: Optional[Dict[str, str]] = None,
            proxy: Optional[str] = None,
            timeout: Optional[int] = None,                        
        ):

        if isinstance(team_id, TeamID):
            team_id = team_id.value

        url = self.BASE_URL.format(team_id=team_id, season=season)
        super().__init__(
            url=url, 
            parser=TeamScheduleParser,
            headers=headers,
            proxy=proxy,
            timeout = timeout,
        )
