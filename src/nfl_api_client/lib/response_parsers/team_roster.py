from nfl_api_client.lib.utils import format_date_str

def TeamRosterParser(json_data):
    data = []
    athletes = json_data.get("athletes", [])
    for group in athletes:
        for player in group.get("items", []):
            dob = player.get("dateOfBirth")
            date = None
            if dob:
                try:
                    date = format_date_str(dob)
                except ValueError:
                    pass

            data.append({
                "player_id": int(player.get("id")),
                "first_name": player.get("firstName"),
                "last_name": player.get("lastName"),
                "full_name": player.get("fullName"),
                "weight": int(player.get("weight")),
                "height": int(player.get("height")),
                "age": int(player.get("age")) if player.get("age") is not None else None,
                "date_of_birth": date or None,
                "college": player.get("college", {}).get("name"),
                "jersey_number": player.get("jersey"),
                "position_name": player.get("position", {}).get("displayName"),
                "position_abbreviation": player.get("position", {}).get("abbreviation"),
                "experience": player.get("experience", {}).get("years", {}) or 0,
                "image_url": player.get("headshot", {}).get("href", {}),
            })
    
    return {
        "TEAM_ROSTER": data  
    }
