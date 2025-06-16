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
                "PLAYER_ID": player.get("id"),
                "FIRST_NAME": player.get("firstName"),
                "LAST_NAME": player.get("lastName"),
                "FULL_NAME": player.get("fullName"),
                "WEIGHT": int(player.get("weight")),
                "HEIGHT": int(player.get("height")),
                "AGE": player.get('age'), 
                "DOB": date or None,
                "DEBUT_YEAR": player.get("debutYear") or None,
                "COLLEGE": player.get("college", {}).get("name"),
                "JERSEY_NUMBER": player.get("jersey"),
                "POSITION_NAME": player.get("position", {}).get("displayName"),
                "POSITION_ABBREVIATION": player.get("position", {}).get("abbreviation"),
                "POSITION_TYPE": player.get("position", {}).get("parent", {}).get("abbreviation"),
                "EXPERIENCE": player.get("experience", {}).get("years", {}) or 0,
                "SLUG": player.get("slug"),
                "IMAGE_URL": player.get("headshot", {}).get("href", {}),
            })
    
    return {
        "ROSTER": data  
    }
