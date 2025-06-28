from nfl_api_client.lib.utils import extract_id_from_ref

def GameOfficialsParser(data):
    items = data.get("items", [])
    result = []
    officials_object = {}
    game_id = extract_id_from_ref(items[0].get('$ref'), "events")
    officials_object['game_id'] = str(game_id)
    for item in items:
        officials_object[item.get('position', {}).get('name', '').lower().replace(' ', '_')] = item.get('displayName')
    result.append(officials_object)

    return {"GAME_OFFICIALS": result}