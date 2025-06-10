import httpx 
import json

HEADERS_CONFIG = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/123.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
}

class EndpointBase:
    def __init__(self, url, parser = None, proxy = None, headers = None, timeout = None):
        self.url = url
        self.parser = parser
        self.proxy = proxy
        self.headers = headers or HEADERS_CONFIG
        self.timeout = timeout or 30
        self.data = None
        self.raw_json = None
        self._fetch_and_parse()

    def get_url(self):
        return self.url
    
    def get_dict(self):
        return self.data

    def get_json(self):
        return json.dumps(self.data)

    def get_df(self):
        import pandas as pd
        return pd.DataFrame(self.data)
    
    # For testing the raw JSON returned from ESPN endpoints
    def get_raw_json(self):
        return self.raw_json
    
    def _fetch_and_parse(self):
        response = httpx.get(
            self.url,
            # proxies=self.proxy,
            headers=self.headers,
            timeout=self.timeout,
        )
        response.raise_for_status()
        self.raw_json = response.json()
        self.data = self.parser(self.raw_json) if self.parser else self.raw_json   

    

