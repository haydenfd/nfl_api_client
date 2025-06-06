from nfl_api.static.players import (
    find_players_by_first_name,
    find_players_by_last_name,
    find_players_by_full_name,
    find_player_by_id,
    get_players,
)

def print_results(title, results):
    print(f"\n=== {title} ===")
    for player in results:
        print(player)

if __name__ == "__main__":
    # Find all Patrick by first name
    first_name_results = find_players_by_first_name("Patrick")
    print_results("First Name = Patrick", first_name_results)

    # Find all Jackson as last name
    last_name_results = find_players_by_last_name("Jackson")
    print_results("Last Name = Jackson", last_name_results)

    # Find Derrick Henry
    full_name_results = find_players_by_full_name("Derrick Henry")
    print_results("Full Name = Derrick Henry", full_name_results)

    # Trevor Lawrence
    player = find_player_by_id(4360310)
    print("\n=== Find by ID = 4360310 ===")
    print(player)

    # All players whose name contains III
    suffix_results = find_players_by_last_name(r"III")
    print_results("III", suffix_results)

    # Print first 5 total players
    all_players = get_players()
    print("\n=== First 5 Players ===")
    for p in all_players[:5]:
        print(p)
