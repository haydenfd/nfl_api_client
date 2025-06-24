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
    ):
        self._name = name
        self._data = data

    @property
    def name(self) -> str:
        return self._name
    
    def get_json(self) -> str:
        import json
        return json.dumps(self._data, indent=2)
    
    def get_dict(self) -> List[Dict]:
        return self._data
    
    def get_dataframe(self) -> Optional[DataFrame]:
        if not pandas:
            raise ImportError("pandas is not installed")

        if not self._data:
            return DataFrame()
        
        return DataFrame(self._data)
