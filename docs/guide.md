# Guide

This guide will go over how to use each endpoint to access data, and what the data access features are. 
<!-- 
## Data Access Patterns

The package is structured such that each endpoint returns a container of datasets. Depending on the nature of the endpoint, this container may hold either one or multiple different datasets. A dataset in this context is a related grouping of data. For example, a team will have 3 different datasets for its depth chart - Offense, Defense, and Special Teams. 

To access the individual datasets, you must first get the particular dataset by name. 

Then, there are 3 utility functions to render the data in your desired format - `get_json()`, `get_dict()`, and `get_dataframe()`. 


```python
# Call endpoint, which loads the dataset container
team_depth_chart = TeamDepthChart(team_id = 12) 

# Access the desired dataset 
offense = team_depth_chart.get_dataset_by_name("OFFENSE") 

 # Print out dataset in dataframe format 
print(offense.get_dataframe())
```

Conversely, you can also chain the above functions. 

```python
TeamDepthChart(team_id = 12).get_dataset_by_name("OFFENSE").get_dataframe()
```

The documentation for each endpoint is structured such that it lists all available datasets under that endpoint, and the individual headers/columns/keys in the returned data. 

You can also view all available dataset names inside a container by using `get_all_dataset_names()` on the particular endpoint object. 
For example, 

```python
TeamDepthChart(team_id = 12).get_all_dataset_names() 
# OUTPUT: ["OFFENSE", "DEFENSE", "SPECIAL_TEAMS"]
```


### Raw ESPN response

This package parses the JSON data returned from ESPN's API endpoints into a well-formed response. A large chunk of each returned response is thrown away by these parsers for lack of relevancy. However, if you would like to access the raw JSON that is returned, you can use `get_raw_json()` at the endpoint level. 


```python
PlayerCareerStats(player_id = 3139477).get_raw_json() 
# OUTPUT: Big JSON load
```

If you would like to access the exact URL that the request is being made to, you can also access `get_url()` at the endpoint level. 
This will return a string of the URL with the query and path parameters embedded. You can copy-paste this URL into your browser or a cURL client such as Postman to inspect the response. 


```python
PlayerCareerStats(player_id = 3139477).get_url() 
# OUTPUT: "https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/athletes/3139477/stats?seasontype=2"
```





## **Package Structure**

Each class invocation => Specific endpoint -> RequestService makes HTTP call -> Response is parsed -> Data is stored in a Dataset container -> Each segmented data set is its own "object".

??? note "Under the hood"
    Each specific endpoint inherits from a base class that handles calling the request service. This base class is also fed a parser specific to the endpoint, which returns the data in the format that you see it when accessing endpoints. 

The endpoint docs are structured in a manner to expose you to each dataset returned by the endpoint, and the headers/columns returned for each data set. Depending on the nature of the endpoint, there might be 1 or multiple data sets. To access each dataset, use `get_dataset(<INSERT NAME>)`. 

On accessing each data set, you have three utility functions that can be used to return data in the desired format. These include - `get_dict()`, `get_json()`, and `get_dataframe()`. 

### Raw data

This package processes the raw ESPN JSON data into a consistent, structured format. In each call, there are often more data points that are pruned since we believe they might not be relevant to the use case. However, for sake of allowing you to custom filter this data however you see fit, each endpoint also comes with a `get_raw_json()` utility function that returns the raw data that ESPN sends. This allows you to do whatever you see fit with the data. Here is how you would access this function. 


### Player & Team IDs

Player IDs for both active and inactive players is accessible as a list through the static. 

Limitation - ESPN only holds information for years past around the 1980s, which shouldn't be an issue for virtually all use-cases but is worth mentioning. 

For IDs pertinent to teams, you can either directly inject the integer values of each team (See full list here), or you can make use of the enum we have provided to directly inject the values based on the team's code. Here is how to use that. 
 -->
