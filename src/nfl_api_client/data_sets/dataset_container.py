from typing import List, Optional
from .dataset import DataSet 


class DataSetContainer:
    def __init__(self, data_sets: Optional[List[DataSet]] = None):
        self._data_sets = data_sets or []

    def add(self, data_set: DataSet):
        self._data_sets.append(data_set)

    def get_all(self) -> List[DataSet]:
        return self._data_sets

    def get_by_name(self, name: str) -> Optional[DataSet]:
        for ds in self._data_sets:
            if ds.name.lower() == name.lower():
                return ds
        return None

    def get_data_frames(self):
        return [ds.get_data_frame() for ds in self._data_sets]

    def get_dicts(self):
        return [ds.get_dict() for ds in self._data_sets]

    def get_jsons(self):
        return [ds.get_json() for ds in self._data_sets]

    def __len__(self):
        return len(self._data_sets)

    def __iter__(self):
        return iter(self._data_sets)

    def __getitem__(self, index: int) -> DataSet:
        return self._data_sets[index]
