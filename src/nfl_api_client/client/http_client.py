import httpx
import asyncio
from typing import List
from nfl_api_client.lib.endpoint_registry import EspnBaseDomain

HEADERS_CONFIG = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}

class EspnRequestService:
    def __init__(self, base_url: EspnBaseDomain, timeout: int = 30, headers: dict = None, proxy: str = None):
        self.base_url = base_url.value.rstrip("/")
        self.timeout = timeout
        self.proxy = proxy 
        self.headers = headers or HEADERS_CONFIG

    def send_request(self, path: str, params=None):
        url = f"{self.base_url}/{path.lstrip('/')}"
        with httpx.Client(timeout=self.timeout, headers=self.headers) as client:
            response = client.get(url, params=params)
        return response.json()

    async def _send_concurrent_requests(self, urls: List[str]):
        async with httpx.AsyncClient(timeout=self.timeout, headers=self.headers) as client:
            tasks = [client.get(url) for url in urls]
            responses = await asyncio.gather(*tasks)
            return [r.json() for r in responses]

    def send_concurrent_requests(self, urls: List[str]):
        return asyncio.run(self._send_concurrent_requests(urls))
