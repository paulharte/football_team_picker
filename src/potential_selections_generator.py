from src.team_selection import TeamSelection

MAX_ITERATIONS = 10000


def generate_all_possible_selections(players_available: list) -> []:
    """ Given a list of player names, it will return all the different ways they can  be split into
        two equal teams. Can also handle odd numbers, where one side has more than the other """
    potential_selections = []
    total_num_players = len(players_available)
    number_to_pick = int(total_num_players / 2.0)

    """ We use a list of booleans to represent the different permutations. 
        True: they are on the first team, False: the second """
    for i in range(MAX_ITERATIONS):
        arr = generate_bool_array(i, total_num_players)
        if arr.count(True) == number_to_pick:
            selection = _form_selection(players_available, arr)
            potential_selections.append(selection)

        if arr.count(True) == total_num_players:
            # Exit when we have exhausted the full boolean range
            break

    return potential_selections


def generate_bool_array(num: int, total_length: int) -> list:
    """ Use bitwise operators to generate the permutations """
    return [bool(num & (1 << n)) for n in range(total_length)]


def _form_selection(players_available: list, permutations: list) -> TeamSelection:
    selection = TeamSelection()
    for player_index in range(len(players_available)):
        if permutations[player_index]:
            selection.white.append(players_available[player_index])
        else:
            selection.black.append(players_available[player_index])
    return selection
