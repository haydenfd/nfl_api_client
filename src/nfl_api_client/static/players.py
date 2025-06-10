import re
import unicodedata
from nfl_api_client.lib.data import (
    players,
    player_id_idx,
    player_first_name_idx,
    player_last_name_idx,
    player_full_name_idx,
    player_active_idx,
)


def _strip_accents(inputstr: str) -> str:
    """
    Normalize and remove accents from string.
    """
    normalizedstr = unicodedata.normalize('NFD', inputstr)
    return ''.join(charx for charx in normalizedstr if unicodedata.category(charx) != 'Mn')


def _find_players(regex_pattern, row_idx):
    players_found = []
    for player in players:
        if re.search(_strip_accents(regex_pattern), _strip_accents(str(player[row_idx])), flags=re.I):
            players_found.append(_get_player_dict(player))
    return players_found


def _get_player_dict(player_row):
    return {
        "id": player_row[player_id_idx],
        "full_name": player_row[player_full_name_idx],
        "first_name": player_row[player_first_name_idx],
        "last_name": player_row[player_last_name_idx],
        "is_active": player_row[player_active_idx],
    }


def find_players_by_full_name(regex_pattern):
    return _find_players(regex_pattern, player_full_name_idx)


def find_players_by_first_name(regex_pattern):
    return _find_players(regex_pattern, player_first_name_idx)


def find_players_by_last_name(regex_pattern):
    return _find_players(regex_pattern, player_last_name_idx)


def find_player_by_id(player_id):
    matches = _find_players(f"^{player_id}$", player_id_idx)
    if len(matches) > 1:
        raise Exception("Found more than 1 id")
    return matches[0] if matches else None


def get_players():
    return [_get_player_dict(player) for player in players]
