# Overview

Each endpoint fetches data from ESPN, then parses the response into structured datasets inside a `DataSetContainer`. This container holds one or more named datasets (each as a list of dictionaries).

You can access:
- the **request URL** via `get_url()`
- the **raw response** via `get_raw_json()`
- the parsed container via `get_data()`

From the container, you can:
- Get a specific dataset with `get_dataset_by_name()`
- List available datasets with `get_all_dataset_names()`

Each `DataSet` lets you:
- View as a list of dicts via `get_dict()`
- View as JSON via `get_json()`
- Convert to a DataFrame via `get_dataframe()`


