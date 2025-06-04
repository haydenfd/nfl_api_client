# src/nfl_api/endpoints/base.py
from nfl_api.client.http_client import EspnRequestService
# from nfl_api.lib.domain_registry import EspnBaseDomain

class Endpoint:
    endpoint: str = ""
    espn_response = None
    url = None

    def __init__(
        self,
        proxy=None,
        headers=None,
        timeout=30,
        get_request=True,
    ):
        self.proxy = proxy
        self.headers = headers
        self.timeout = timeout

        if get_request:
            self.get_request()

    def get_request(self):
        client = EspnRequestService(
            base_url=self.base_domain,
            proxy=self.proxy,
            headers=self.headers,
            timeout=self.timeout,
        )
        self.response = client.send_request(self.endpoint)

    def get_dict(self):
        return self.response

    def get_url(self):
        return self.url
