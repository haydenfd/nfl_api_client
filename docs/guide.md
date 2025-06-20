# Guide

This guide will go over how to use each endpoint to access data, and what the data access features are. 


## **Package Structure**

??? info "Package Structure Overview"

    ```mermaid
    graph LR
      A[Specific Endpoint Class] --> B[Parses Raw Response]
      B --> C[Each 'Grouping' is a DataSet]
      C --> D[Returns List of DataSets]
    ```


Each class invocation => Specific endpoint -> RequestService makes HTTP call -> Response is parsed -> Data is stored in a Dataset container -> Each segmented data set is its own "object".

??? note "Under the hood"
    Each specific endpoint inherits from a base class that handles calling the request service. This base class is also fed a parser specific to the endpoint, which returns the data in the format that you see it when accessing endpoints. 

The endpoint docs are structured in a manner to expose you to each dataset returned by the endpoint, and the headers/columns returned for each data set. Depending on the nature of the endpoint, there might be 1 or multiple data sets. To access each dataset, use `get_dataset(<INSERT NAME>)`. 

On accessing each data set, you have three utility functions that can be used to return data in the desired format. These include - `get_dict()`, `get_json()`, and `get_data_frame()`. 

### Raw data

This package processes the raw ESPN JSON data into a consistent, structured format. In each call, there are often more data points that are pruned since we believe they might not be relevant to the use case. However, for sake of allowing you to custom filter this data however you see fit, each endpoint also comes with a `get_raw_json()` utility function that returns the raw data that ESPN sends. This allows you to do whatever you see fit with the data. Here is how you would access this function. 


### Player & Team IDs

Player IDs for both active and inactive players is accessible as a list through the static. 

Limitation - ESPN only holds information for years past around the 1980s, which shouldn't be an issue for virtually all use-cases but is worth mentioning. 

For IDs pertinent to teams, you can either directly inject the integer values of each team (See full list here), or you can make use of the enum we have provided to directly inject the values based on the team's code. Here is how to use that. 


## **Request Configuration**


### Default request parameters 

By default, all requests are routed with no proxy URL and with a timeout set to 10 seconds, which we have found is ample time. These are the headers used:

```python
"User-Agent":   "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                "AppleWebKit/537.36 (KHTML, like Gecko)"
                "Chrome/123.0.0.0 Safari/537.36",

"Accept": "application/json",

"Accept-Language": "en-US,en;q=0.9",
```
<br>
### Customize your requests

You can also set custom HTTP request headers, proxy URLs, and a timeout with each request sent to an endpoint. These three variables can be specified in each function call as parameters. The endpoint documentation under the API reference excluded including these for brevity. This allows you to have more fine-grained control over your requests. Additionally, in cases where your requests *might* be blocked from a cloud provider such as AWS (we have not confirmed that this is the case) and would need a proxy to route requests through. 


If you would like to set custom configurations, here is how you would do it: 


```python

custom_headers = {...}
proxy_url =  "https://fakeproxy.com"
extended_timeout = 30

sample_stats = PlayerCareerStats(
    player_id=4262921,
    headers = custom_headers,
    proxy = proxy_url,
    timeout = extended_timeout,
    )
```

!!! NOTE

    These 3 request parameters must be set by **keyword** arguments only. Doing something like (custom_headers, proxy, timeout) without specifying the "headers = ", for instance, will return an error! This is a deliberate design choice to avoid confusion when setting custom configs. 
