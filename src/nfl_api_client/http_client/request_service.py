import httpx
import asyncio
from typing import List, Optional, Dict, Union
import sys

DEFAULT_HEADER_CONFIG = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/123.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
}


# SEE: https://www.python-httpx.org/advanced/proxies/ for proxy docs

class HttpxRequestService:
    def __init__(
        self, 
        *, # Enforces keyword args when passing in args
        headers: Optional[Dict[str, str]] = None, 
        timeout: int = 10, 
        proxy: Optional[str] = None
    ):
        self.headers = headers or DEFAULT_HEADER_CONFIG
        self.timeout = timeout
        self.proxy = proxy
    

    def send_request(self, url: str) -> Union[Dict, None]:

        try:
            with httpx.Client(
                headers=self.headers,
                proxy=self.proxy,
                timeout=self.timeout,
            ) as client:
                response = client.get(url)
                # print(url)
                response.raise_for_status()
                # print(response.json())
                return response.json()
            
        except httpx.HTTPStatusError as e: 
            if e.response.status_code == 404:
                print(f"Error: Request URL is not valid. Please check the arguments you have provided.")
                sys.exit(1)
            else: 
                print(f"Error: HTTP error {e.response.status_code}: {e.request.url}")
        except httpx.TimeoutException as e:
            print(f"Error: Request to url {url} timed out")
        except httpx.RequestError as e:
            print(f"Error: Network error while requesting {url}: {e}")
        except Exception as e:
            print(f"Error: Unexpected error: {e}")
        return None


    def send_concurrent_requests(self, urls: List[str]) -> List[dict]:
        async def _fetch_all():
            async with httpx.AsyncClient(
                timeout=self.timeout,
                headers=self.headers,
                proxy=self.proxy,
            ) as client:
                tasks = [client.get(url) for url in urls]
                responses = await asyncio.gather(*tasks, return_exceptions=True)

                result = []
                for r in responses:
                    if isinstance(r, Exception):
                        print(f"Error: Request failed: {r}")
                        result.append({})
                    elif r.is_error:
                        print(f"Error: HTTP error {r.status_code} for {r.url}")
                        result.append({})
                    else:
                        try:
                            result.append(r.json())
                        except Exception as e:
                            print(f"Error: Failed to parse JSON for {r.url}: {e}")
                            result.append({})
                return result

        try:
            return asyncio.run(_fetch_all())
        except RuntimeError as e:
            if "event loop is running" in str(e):
                return asyncio.get_event_loop().run_until_complete(_fetch_all())
            raise