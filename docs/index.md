# **NFL API Client**

Welcome to the documentation for the `nfl_api_client` (Current version: 1.0.0).

## **About**

`nfl_api_client` provides a simple and flexible interface to query ESPN's NFL data endpoints. Whether you're building tools, performing research, or just exploring stats, this package makes it easy to retrieve exactly the NFL data you need.

**Key Features**:

- Rich documentation with examples for each endpoint
- Fully configurable HTTP requests
- Access to raw ESPN responses and resolved request URLs


!!! Note
    This package is currently in active development. While many endpoints are implemented (such as rosters, depth charts, standings, and stats), others are still in the works. You can track the CHANGELOG for more updates. 

## **Getting Started**

### Installation

Python `3.9+` is required. The package depends on `httpx` and pandas.

To install the package and its dependencies, run 

```python
pip install nfl-api-client
```

### Table Of Contents

- Guide: Includes how to go about accessing data returned from endpoints, static data like player and team IDs, and customizing your HTTP requests. 
- Reference: Documentation for various endpoints. 
- CHANGELOG: Updates made to package source code. 


## **Contributing**

There are many endpoints that still need to be built out. If you would like to contribute, please send an email to **haydenfds@gmail.com**. Everyone is welcome!

## **License**

This package is provided for use under the MIT license.  

ESPN's current TOS doesn't seem to prohibit the use or publishing of such a package, but nevertheless, please be responsible when using it. 