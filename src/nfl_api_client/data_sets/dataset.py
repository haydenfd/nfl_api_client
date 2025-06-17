import json
from typing import Any, List, Dict, Optional

try:
    import pandas
    from pandas import DataFrame
except ImportError:
    pandas = None


class DataSet:
    '''
    Wraps a group of related data from an endpoint. 
    '''
    def __init__(
            self,
            *,
            name: str,
            data: List[Dict[str, Any]],
            headers: Optional[List[str]] = None, # TODO: Maybe omit?
    ):
        self._name = name
        self.data = data
        self.headers = headers

    @property
    def name(self) -> str:
        return self._name
    
    def get_json(self) -> str:
        return json.dumps(self.data, indent=2)
    
    # TODO: Maybe reformat
    def get_dict(self) -> List[Dict]:
        return self.data
    
    def get_data_frame(self) -> Optional[DataFrame]:
        if not pandas:
            raise ImportError("pandas is not installed")

        if not self.data:
            return DataFrame()

        if self.headers:
            return DataFrame(self.data)[self.headers]
        return DataFrame(self.data)
    
    def get_headers(self) -> List[str]:
        if self.headers:
            return self.headers
        if self.data:
            return list(self.data[0].keys())
        return []