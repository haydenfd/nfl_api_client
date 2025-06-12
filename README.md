# NFL API Client
## API Client Library for access to ESPN's NFL data points

`nfl_api_client` is an API client package that provides easy access to ESPN data about the NFL. We are still actively building out many endpoints and refining existing implementations, but a basic version with certain endpoints is already accessible for your use. 

## Getting Started

This package requires Python 3.8+. `nfl_api_client` uses `httpx` for making requests to the ESPN endpoints, and `pandas/numpy` for viewing and manipulating data in a dataframe format.  

To install the package, simply run  
```{python}
    pip install nfl-api-client
```


## Table of Endpoints

This list consists of actively usable endpoints for various data. It is being continuously updated. 

- [Season Standings](https://github.com/haydenfd/nfl_api_client/blob/main/src/nfl_api_client/endpoints/season_standings.py)
- [Team Depth Chart](https://github.com/haydenfd/nfl_api_client/blob/main/src/nfl_api_client/endpoints/team_depth_chart.py)
- [Team Roster](https://github.com/haydenfd/nfl_api_client/blob/main/src/nfl_api_client/endpoints/team_roster.py)
- [Team Schedule](https://github.com/haydenfd/nfl_api_client/blob/main/src/nfl_api_client/endpoints/team_schedule.py)

## License & Disclaimer

This package is provided for use under the MIT license.  

ESPN's current TOS doesn't seem to prohibit the use or publishing of such a package, but nevertheless, please be responsible when using it. 