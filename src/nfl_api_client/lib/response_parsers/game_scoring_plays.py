def GameScoringPlaysParser(data):
    scoring_plays = data.get("scoringPlays", [])
    parsed = []

    for play in scoring_plays:
        parsed.append({
            "drive_id": play.get("id"),
            "description": play.get("text"),
            "team_id": play.get("team", {}).get("id"),
            "team_code": play.get("team", {}).get("abbreviation"),            
            "home_score": play.get("homeScore"),
            "away_score": play.get("awayScore"),
            "play_type": play.get("type", {}).get("text"),
            "play_abbreviation": play.get("type", {}).get("abbreviation"),
            "period": play.get("period", {}).get("number"),
            "clock": play.get("clock", {}).get("displayValue"),
        })

    return {
        "SCORING_PLAYS": parsed
    }