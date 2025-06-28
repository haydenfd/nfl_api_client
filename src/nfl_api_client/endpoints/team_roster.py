from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
from nfl_api_client.endpoints._base import BaseEndpoint
from nfl_api_client.lib.response_parsers.team_roster import TeamRosterParser
from nfl_api_client.lib.parameters import TeamID
from typing import Union, Optional, Dict

class TeamRoster(BaseEndpoint):
    def __init__(
        self,
        team_id: Union[int, TeamID],
        *,
        headers: Optional[Dict[str, str]] = None,
        proxy: Optional[str] = None,
        timeout: Optional[int] = None,
    ):

        if isinstance(team_id, TeamID):
            team_id = team_id.value

        valid_team_ids = {team.value for team in TeamID}
        if team_id not in valid_team_ids:
            raise ValueError(f"team_id: {team_id} is not a valid ID. Look at Parameters > TeamID for more.")
        url = ENDPOINT_REGISTRY["TEAM_ROSTER"].format(team_id=team_id)
        super().__init__(
            url, 
            parser=TeamRosterParser,
            headers=headers,
            proxy=proxy,
            timeout=timeout,
        )