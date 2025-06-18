# Guide

This guide will go over how to use each endpoint to access data, and what the data access features are. 



## Request Configuration


### Default request parameters 

By default, all requests are routed with no proxy URL and with a timeout set to 10 seconds, which we have found is ample time. However, feel free to set a longer timout if needed. These are the headers used:

```python
"User-Agent":   "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                "AppleWebKit/537.36 (KHTML, like Gecko)"
                "Chrome/123.0.0.0 Safari/537.36",

"Accept": "application/json",

"Accept-Language": "en-US,en;q=0.9",
```

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
