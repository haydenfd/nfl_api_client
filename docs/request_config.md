# HTTP Request Configuration

## **Default Request Parameters**

By default, all requests are made **without a proxy** and use a **10-second timeout**, which seems to be a sufficient value in most cases. The following HTTP headers are sent with each request:

```python
"User-Agent":   ("Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                "AppleWebKit/537.36 (KHTML, like Gecko)"
                "Chrome/123.0.0.0 Safari/537.36",
                ),

"Accept": "application/json",

"Accept-Language": "en-US,en;q=0.9",

```

## **Customize Requests**

For more fine-grained control over your requests, you can override the default behavior by supplying custom values for - 
    <br><br> 
    - **HTTP headers** (`headers`)  
    - **Proxy URL** (`proxy`)  
    - **Request timeout in seconds** (`timeout`) 

This flexibility can be useful if you are - <br><br>
- Routing through a proxy (e.g. to bypass rate limits or regional restrictions),  
- Experiencing slow endpoints that require extended timeouts,  
- Using a cloud provider (like AWS), where ESPN *may* block requests from those IP addresses. If this happens, it might be useful to configure a separate proxy. 

<br> 

!!! NOTE
    These parameters can be passed in for **all endpoints**, but are omitted from the reference documentation for brevity.
<br>

Here’s how you can provide custom parameters:


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

<br> 

!!! NOTE
    All three request parameters must be passed as **keyword arguments**.<br><br>
    For example, *PlayerCareerStats(custom_headers, proxy_url, 30)* will throw an error. 
    <br><br> 
    This is an intentional design choice to prevent ambiguity when setting request configurations.