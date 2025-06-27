# **NFL API Client**

Welcome to the documentation for the `nfl_api_client` (Current version: 1.0.0).

## **About**

`nfl_api_client` is a Python package that provides a simple and flexible interface for accessing ESPN's NFL data. This package makes it easy to fetch exactly the data points you need. 
Features: 
    - Elaborate documentation with examples for each endpoint. 
    - Ability to configure your HTTP requests.
    - Access to the raw ESPN response data and request URLs. 


!!! Note
    This package is currently in active development. While many endpoints are implemented (such as rosters, depth charts, standings, and stats), others are still in the works. You can track the CHANGELOG for more updates. 

## **Getting Started**

### Installation

This package requires Python `3.9+` and uses `httpx` and `pandas` as dependencies for fetching and processing the data.

To install the package and its dependencies, run 

```python
pip install nfl-api-client
```

### Table Of Contents

- Guide: Includes how to go about accessing data returned from endpoints, static data like player and team IDs, and customizing your HTTP requests. 
- Reference: Documentation for various endpoints. 


## **Contributing**

There are many endpoints that still need to be built out. If you would like to contribute, please send an email to haydenfds@gmail.com. Everyone is welcome!

## **License**

This package is provided for use under the MIT license.  

ESPN's current TOS doesn't seem to prohibit the use or publishing of such a package, but nevertheless, please be responsible when using it. 