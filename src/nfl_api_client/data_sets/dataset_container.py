from typing import List, Optional, Dict
from .dataset import DataSet 


class DataSetContainer:
    def __init__(self, data_sets: List[DataSet]):
        self._data_sets = {ds.name: ds for ds in data_sets}

    def __len__(self):
        return len(self._data_sets)

    def __iter__(self):
        return iter(self._data_sets.values())

    def get_by_name(self, name: str) -> DataSet:
        return self._data_sets[name.upper()]

    def get_all(self) -> Dict[str, DataSet]:
        return self._data_sets