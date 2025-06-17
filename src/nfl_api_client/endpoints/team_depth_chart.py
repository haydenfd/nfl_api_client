from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
from nfl_api_client.endpoints._base import BaseEndpoint
from nfl_api_client.lib.response_parsers.team_depth_chart import TeamDepthChartParser
from nfl_api_client.lib.parameters import TeamID
from typing import Union, Optional, Dict

class TeamDepthChart(BaseEndpoint):
    # """
    # Fetches the depth chart for a given NFL team and season.

    # This endpoint returns positional information (offense, defense, and special teams)
    # for all athletes listed in a team's depth chart during a specific season.
    # The response is organized into three datasets: `"OFFENSE"`, `"DEFENSE"`, and `"SPECIAL_TEAMS"`.

    # Each dataset can be accessed via `.get_dataset("OFFENSE")`, etc., and supports rich utility methods
    # such as `.get_data_frame()`, `.get_dict()`, `.get_headers()`, and `.get_json()`.

    # Args:
    #     team_id (Union[int, TeamID]): The ESPN NFL team ID, or a member of the `TeamID` enum.
    #     year (int): The target season year in `YYYY` format.
    #     headers (Optional[Dict[str, str]]): Optional headers to pass with the HTTP request.
    #     proxy (Optional[str]): Optional proxy string for routing the request.
    #     timeout (Optional[int]): Timeout (in seconds) for the HTTP request.

    # Example:
    #     ```python
    #     from nfl_api_client.endpoints.team_depth_chart import TeamDepthChart
    #     from nfl_api_client.lib.parameters import TeamID

    #     # Either works:
    #     chart = TeamDepthChart(team_id=12, year=2024)
    #     # chart = TeamDepthChart(team_id=TeamID.KC, year=2024)

    #     # Get the offensive depth chart as a DataFrame
    #     offense_df = chart.get_dataset("OFFENSE").get_data_frame()
    #     print(offense_df.head())

    #     # Get the defensive chart headers
    #     defense_headers = chart.get_dataset("DEFENSE").get_headers()
    #     print(defense_headers)

    #     # View the full request URL used
    #     print(chart.get_url())
    #     ```

    # Returns:
    #     The object holds an internal dataset container with 3 datasets:
    #         - `"OFFENSE"`
    #         - `"DEFENSE"`
    #         - `"SPECIAL_TEAMS"`

    #     Each dataset contains the following fields:
    #         - `PLAYER_ID`: ESPN Player ID
    #         - `PLAYER_NAME`: Player name        
    #         - `POSITION_NAME`: Position name
    #         - `POSITION_ABBREVIATION`: Position abbreviation
    #         - `RANK`: Positional rank
    # """    
    def __init__(
            self, 
            team_id: Union[int, TeamID], 
            year: int,
            *,
            headers: Optional[Dict[str, str]] = None,
            proxy: Optional[str] = None,
            timeout: Optional[int] = None,            
        ):

        if isinstance(team_id, TeamID):
            team_id = team_id.value        

        url = ENDPOINT_REGISTRY["TEAM_DEPTH_CHART"].format(team_id=team_id, year=year)
        super().__init__(
            url, 
            parser=TeamDepthChartParser,
            headers=headers,
            proxy=proxy,
            timeout=timeout,
        )

chart = TeamDepthChart(team_id=33, year=2024)

offense_df = chart.get_dataset("OFFENSE").get_data_frame()
print(offense_df.head())

defense_headers = chart.get_dataset("DEFENSE").get_headers()
print(defense_headers)

print(chart.get_url())