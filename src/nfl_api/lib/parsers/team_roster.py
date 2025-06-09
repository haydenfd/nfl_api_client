from nfl_api.lib.utils import format_date_str

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
                "player_id": player.get("id"),
                "first_name": player.get("firstName"),
                "last_name": player.get("lastName"),
                "full_name": player.get("fullName"),
                "weight": int(player.get("weight")),
                "height": int(player.get("height")),
                "age": player.get('age'), 
                "date_of_birth": date or None,
                "debut_year": player.get("debutYear") or None,
                "college": player.get("college", {}).get("name"),
                "jersey_number": player.get("jersey"),
                "position_abbreviation": player.get("position", {}).get("abbreviation"),
                "position_type": player.get("position", {}).get("parent", {}).get("abbreviation"),
                "experience": player.get("experience", {}).get("years", {}) or 0,
                "slug": player.get("slug"),
                "image_href": player.get("headshot", {}).get("href", {}),
            })
    return data
