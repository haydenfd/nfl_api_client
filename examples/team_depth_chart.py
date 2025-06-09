from nfl_api.endpoints.team_depth_chart import TeamDepthChart

if __name__ == "__main__":
    data = TeamDepthChart(12, 2024)
    print(data.get_raw_json())
    print(data.get_df())
