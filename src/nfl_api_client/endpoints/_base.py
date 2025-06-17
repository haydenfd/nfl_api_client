import json
from typing import Optional, Callable, Dict, Any, List, Union

from nfl_api_client.http_client.request_service import HttpxRequestService
from nfl_api_client.data_sets.dataset import DataSet
from nfl_api_client.data_sets.dataset_container import DataSetContainer

import pandas as pd

from nfl_api_client.http_client.request_service import HttpxRequestService
from nfl_api_client.data_sets.dataset import DataSet
from nfl_api_client.data_sets.dataset_container import DataSetContainer


class BaseEndpoint:
    def __init__(
        self,
        url: str,
        *,
        parser: Optional[Callable[[Dict[str, Any]], Union[Dict[str, List[Dict]], List[Dict]]]] = None,
        proxy: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = 10
    ):
        self.url = url
        self.parser = parser
        self.proxy = proxy
        self.headers = headers
        self.timeout = timeout
        self.raw_json = None
        self.data_sets: Optional[DataSetContainer] = None

        self.request_service = HttpxRequestService(headers=self.headers, timeout=self.timeout, proxy=self.proxy)
        self._fetch_and_parse()

    def _fetch_and_parse(self):
        self.raw_json = self.request_service.send_request(self.url)
        parsed = self.parser(self.raw_json) if self.parser else self.raw_json

        if isinstance(parsed, dict):
            self.data_sets = DataSetContainer([
                DataSet(name=k, data=v) for k, v in parsed.items()
            ])
        elif isinstance(parsed, list):
            self.data_sets = DataSetContainer([
                DataSet(name="DEFAULT", data=parsed)
            ])
        else:
            raise ValueError("Parsed data must be a dict or list.")

    def get_dataset(self, name: str) -> DataSet:
        return self.data_sets.get_by_name(name)

    def get_data_sets(self) -> DataSetContainer:
        return self.data_sets

    def get_raw_json(self) -> Dict[str, Any]:
        return self.raw_json

    def get_url(self) -> str:
        return self.url

    def get_dict(self) -> Dict[str, Any]:
        return {
            ds.name: ds.get_dict()
            for ds in self.data_sets
        }

    def get_json(self) -> str:
        return json.dumps(self.get_dict(), indent=2)

    def get_data_frame(self, name: Optional[str] = None) -> Union[pd.DataFrame, Dict[str, pd.DataFrame]]:
        if not self.data_sets:
            return None
        if name:
            return self.get_dataset(name).get_data_frame()
        return {ds.name: ds.get_data_frame() for ds in self.data_sets}