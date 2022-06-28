from itertools import product
from collections import Counter
from functools import reduce

# Scores table
game_score = {
    "Brian": {"game1": 1, "game2": 0, "game3": 5, "game4": 1},
    "David": {"game1": 2, "game2": 1, "game3": 0, "game4": 2},
    "John": {"game1": 0, "game2": 2, "game3": 4, "game4": 2},
}
# Designated the criteria of game max scores
maxima = {"game1": 2, "game2": float('inf'), "game3": 2, "game4": 2}


# Generate a table of all binary combinations for n positions
def make_binary_combos(n):
    return [i for i in product(range(2), repeat=n)]


# Goes to generate all possible combinations for a given n and bound
# by a maxima that can be empty in case there's no maxima
def generate_all_game_combos(game_score, n, maxima={}):
    # Verify that n is positive integer != 0
    assert (n > 0 and isinstance(n, int)),\
        "N must be a positive non-zero integer"

    if maxima:
        players = list(game_score.keys())
        # Verify that the maxima game names
        # is the same as those in the games scores
        assert len(maxima.keys()) == len(game_score[players[0]]),\
            "Maxima list must have the same length as number of games."
        assert maxima.keys() == game_score[players[0]].keys(),\
            "Maxima Games must have the same identifiers as games in scores"

    output_cases = dict()
    # The case of n == 1 is simply one player at a time
    if n == 1:
        for key in game_score.keys():
            if maxima:
                x, y = maxima, game_score.get(key)
                output_cases[key] = {
                    k: max(x[k], y[k]) if x[k] <= y[k] else y[k] for k in x
                }
            else:
                output_cases[key] = game_score.get(key)
    # When we have n >= 2
    else:
        # Call the binary combinations generator
        bin_combos = make_binary_combos(len(game_score.keys()))
        # Search for cases where number of people is as n
        # i.e. the sum of binary value in that case is n
        bin_sums = list(map(sum, bin_combos))
        valid_cases = [i for i, x in enumerate(bin_sums) if x == n]
        # Generate a dictionary for the valid combos one by one
        for valid_case in valid_cases:
            key, value = make_combo_dict(
                game_score,
                bin_combos[valid_case],
                maxima
            )
            output_cases[key] = value

    return output_cases


def make_combo_dict(game_score, combo, maxima=[]):
    # Search for players names in the games scores
    players = list(game_score.keys())
    # build the key of the combination
    dict_key = [players[i] for i, x in enumerate(combo) if x == 1]
    # Build an empty dictionary similar to
    # the one of games initialized to 0 everywhere
    dict_item = dict.fromkeys(game_score[players[0]].keys(), 0)

    # Sum up the corresponding selected players scores in the combo
    for dict_key_player in dict_key:
        data = [
            dict_item,
            game_score[dict_key_player]
        ]
        dict_item = dict(reduce(lambda x, y: Counter(x) + Counter(y), data))
        # Check against the maxima criteria
        if maxima:
            x, y = maxima, dict_item
            dict_item = {
                k: x[k] if x[k] <= y[k] else y[k] for k in x if y.get(k, '')
            }
    # Return the key string and the corresponding games scores values
    return ", ".join(dict_key), dict_item


########
# MAIN #
########


# Capture the indexing information
game_score_len = len(game_score.keys())

print("Without maxima ... ")
for n in range(1, game_score_len+1):
    print(f"Case of {n} persons")
    combo_cases = generate_all_game_combos(game_score, n)
    for key in combo_cases.keys():
        print(f" {key} => {combo_cases.get(key)}")

print("\nWith maxima ... ")
for n in range(1, game_score_len+1):
    print(f"Case of {n} persons")
    combo_cases = generate_all_game_combos(game_score, n, maxima)
    for key in combo_cases.keys():
        print(f" {key} => {combo_cases.get(key)}")
