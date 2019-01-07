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


def print_capital(state):
    states_dict, capital_cities_dict = get_dict()
    abbreviation = states_dict.get(state, None)
    capital = capital_cities_dict.get(abbreviation, "Unknown state")
    print(capital)


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        print_capital(args[1])
