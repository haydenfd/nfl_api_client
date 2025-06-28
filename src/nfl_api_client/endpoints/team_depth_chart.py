from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
from nfl_api_client.endpoints._base import BaseEndpoint
from nfl_api_client.lib.response_parsers.team_depth_chart import TeamDepthChartParser
from nfl_api_client.lib.parameters import TeamID
from typing import Union, Optional, Dict

class TeamDepthChart(BaseEndpoint):
    def __init__(
            self, 
            team_id: Union[int, TeamID], 
            year: int = 2025,
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

        url = ENDPOINT_REGISTRY["TEAM_DEPTH_CHART"].format(team_id=team_id, year=year)
        super().__init__(
            url, 
            parser=TeamDepthChartParser,
            headers=headers,
            proxy=proxy,
            timeout=timeout,
        )

# chart = TeamDepthChart(team_id=33, year=2024)

# offense_df = chart.get_dataset("OFFENSE").get_dataframe()
# print(offense_df[offense_df["position_abbreviation"] == "WR"])
