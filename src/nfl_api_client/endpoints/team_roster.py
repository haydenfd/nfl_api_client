from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
from nfl_api_client.endpoints._base import BaseEndpoint
from nfl_api_client.lib.response_parsers.team_roster import TeamRosterParser
from nfl_api_client.lib.parameters import TeamID
from typing import Union, Optional, Dict

class TeamRoster(BaseEndpoint):
    """    
    This endpoint returns the current roster for a given team.

    Currently, it only supports present rosters, but we are actively working towards fetching rosters for any given year. 

    Args:
        team_id (TeamID): ID of the NFL team.
        headers (Dict): Custom headers to use in the HTTP request.
        proxy (str): Proxy to route the HTTP request through.
        timeout (int): Request timeout in seconds (defaults to 10).
        

    Returns:
        Roster dataset. 

    Each item in this dataset is a dictionary with the following structure:
    
    {
        "PLAYER_ID": int,
        "FIRST_NAME": str,
        "LAST_NAME": str,
        "FULL_NAME": str,
        "WEIGHT": int,
        "HEIGHT": int,
        "AGE": int,
        "DOB": str (formatted as "YYYY-MM-DD"),
        "DEBUT_YEAR": Optional[int],
        "COLLEGE": Optional[str],
        "JERSEY_NUMBER": str,
        "POSITION_NAME": str,
        "POSITION_ABBREVIATION": str,
        "POSITION_TYPE": str,
        "EXPERIENCE": int,
        "SLUG": str,
        "IMAGE_URL": Optional[str]
    }

    Example:
        ```python
        from nfl_api_client.endpoints.team_roster import TeamRoster
        from nfl_api_client.lib.parameters import TeamID

        # TeamRoster(team_id=12) also works here since Chiefs have ID = 12

        chiefs_roster = TeamRoster(team_id=TeamID.KC) 

        # ROSTER is the only dataset returned. Access this dataset's dataframe. 

        data_frame = roster.get_dataset("ROSTER").get_data_frame()
        print(df.head())

        # Inspect the headers/columns used in the "ROSTER" dataset
        headers = roster.get_dataset("ROSTER").get_headers()
        print(headers)
        ```
    """
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