import sys


def get_dict():
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    return states, capital_cities


def get_key(dictionary, value):
    for k, v in dictionary.items():
        if v == value:
            return k
    return "Unknown capital city"


def print_state(capital):
    states_dict, capital_cities_dict = get_dict()
    abbreviation = get_key(capital_cities_dict, capital)
    state = get_key(states_dict, abbreviation)
    print(state)


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        print_state(args[1])
