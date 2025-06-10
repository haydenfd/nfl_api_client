import json
from nfl_api_client._client._http_client import HttpxRequestService
from typing import Optional, Dict

class EndpointBase:
    def __init__(
            self, 
            url:str,
            parser = None, 
            proxy = None, 
            headers:Optional[Dict[str, str]] = None, 
            timeout:Optional[int] = None
        ):
        self.url: str = url
        self.parser = parser
        self.proxy = proxy
        self.headers:Optional[Dict[str, str]] = headers 
        self.timeout = timeout or 30
        self.data = None
        self.raw_json = None
        self.request_service: HttpxRequestService = HttpxRequestService(
            headers,
            timeout,
            proxy,
        )
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
        self.raw_json = self.request_service.send_request(self.url)
        self.data = self.parser(self.raw_json) if self.parser else self.raw_json

    

