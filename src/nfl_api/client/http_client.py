import httpx
import asyncio
import time

class HttpClient:
    def __init__(
            self, 
            base_url,
            timeout=30.0, 
            headers=None):
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br', 
            'Connection': 'keep-alive',
        }
        self.timeout = timeout

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        with httpx.Client(headers=self.headers, timeout=self.timeout) as client:
            resp = client.get(url, params=params)
            resp.raise_for_status()
            return resp.json()
    
    async def get_multiple_urls_concurrent(self, endpoints):
        async with httpx.AsyncClient(headers=self.headers, timeout=self.timeout) as client:
            tasks = [
                client.get(f"{self.base_url}/{endpoint.lstrip('/')}")
                for endpoint in endpoints
            ]
            responses = await asyncio.gather(*tasks)
            print(f"Fetching for {len(tasks)} different tasks")
            return [res.json() for res in responses]


# def main():
#     start_time = time.perf_counter()

#     client = HttpClient(
#         base_url="https://sports.core.api.espn.com",
#     )

#     data = client.get("/v2/sports/football/leagues/nfl/athletes/3139477/statisticslog")

#     end_time = time.perf_counter()
#     elapsed = end_time - start_time

#     print(f"\nTime taken: {elapsed:.3f} seconds")
#     print(data)

# if __name__ == "__main__":
#     main()

def main():
    client = HttpClient(
        base_url="https://sports.core.api.espn.com", 
    )
    
    endpoints = [
        "v2/sports/football/leagues/nfl/seasons/2024/types/2/athletes/3139477/statistics/0?lang=en&region=us",
        "v2/sports/football/leagues/nfl/seasons/2023/types/2/athletes/3139477/statistics/0?lang=en&region=us",
        "v2/sports/football/leagues/nfl/seasons/2022/types/2/athletes/3139477/statistics/0?lang=en&region=us",
        "v2/sports/football/leagues/nfl/seasons/2021/types/2/athletes/3139477/statistics/0?lang=en&region=us",
        "v2/sports/football/leagues/nfl/seasons/2020/types/2/athletes/3139477/statistics/0?lang=en&region=us",
        "v2/sports/football/leagues/nfl/seasons/2019/types/2/athletes/3139477/statistics/0?lang=en&region=us",
        "v2/sports/football/leagues/nfl/seasons/2018/types/2/athletes/3139477/statistics/0?lang=en&region=us",
        "v2/sports/football/leagues/nfl/seasons/2017/types/2/athletes/3139477/statistics/0?lang=en&region=us",
    ]

    start = time.perf_counter()
    results = asyncio.run(client.get_multiple_urls_concurrent(endpoints))
    end = time.perf_counter()

    print(f"\nFetched {len(results)} stats in {end - start:.3f} seconds")
    # print(results)

if __name__ == "__main__":
    main()