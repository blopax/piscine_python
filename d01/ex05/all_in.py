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
    return None


def find_state(capital):
    states_dict, capital_cities_dict = get_dict()
    abbreviation = get_key(capital_cities_dict, capital)
    state = get_key(states_dict, abbreviation)
    return state


def find_capital(state):
    states_dict, capital_cities_dict = get_dict()
    abbreviation = states_dict.get(state, None)
    capital = capital_cities_dict.get(abbreviation, None)
    return capital


def clean_double_spaces(string):
    while "  " in string:
        string = string.replace("  ", " ")
    return string


def print_result(arg, clean_arg, capital, state):
    if (capital, state) == (None, None):
        print("{} is neither a capital nor a state".format(arg))
    elif capital is not None:
        print("{} is the capital of {}".format(capital, clean_arg))
    else:
        print("{} is the capital of {}".format(clean_arg, state))


def print_all(string):
    args_list = [clean_double_spaces(arg).strip() for arg in string.split(",") if arg.strip() != '']
    for arg in args_list:
        clean_arg = ' '.join(map(lambda x: x.capitalize(), arg.lower().split()))
        capital = find_capital(clean_arg)
        state = find_state(clean_arg)
        print_result(arg, clean_arg, capital, state)


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        print_all(args[1])
