from typing import List, Optional, Dict
from .dataset import DataSet 


class DataSetContainer:
    def __init__(self, data_sets: List[DataSet]):
        self._data_sets = {ds.name: ds for ds in data_sets}

    def __len__(self):
        return len(self._data_sets)

    def get_dataset(self, name: str) -> DataSet:
        key = name.upper()
        if key not in self._data_sets:
            raise ValueError(f"Dataset '{name}' not found. Available datasets: {', '.join(self._data_sets.keys())}")
        return self._data_sets[key]

    def get_all_dataset_names(self) -> List[str]:
        return list(self._data_sets.keys())
    