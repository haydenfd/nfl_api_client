import httpx
import asyncio
from typing import List, Optional, Dict, Any

DEFAULT_HEADER_CONFIG = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/123.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
}


class HttpxRequestService:
    def __init__(self, headers: Optional[Dict[str, str]] = None, timeout: int = 30, proxy: Optional[str] = None):
        self.headers = headers or DEFAULT_HEADER_CONFIG
        self.timeout = timeout
        self.proxy = proxy

    def send_request(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict:
        with httpx.Client(timeout=self.timeout, headers=self.headers) as client:
            response = client.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def send_concurrent_requests(self, urls: List[str]) -> List[Dict]:
        async def _fetch_all():
            async with httpx.AsyncClient(timeout=self.timeout, headers=self.headers) as client:
                tasks = [client.get(url) for url in urls]
                responses = await asyncio.gather(*tasks)
                return [r.json() for r in responses]

        try:
            return asyncio.run(_fetch_all())
        except RuntimeError as e:
            if "event loop is running" in str(e):
                return asyncio.get_event_loop().run_until_complete(_fetch_all())
            raise