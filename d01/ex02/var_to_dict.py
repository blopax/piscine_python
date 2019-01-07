def get_dict_list():
    d = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]
    return d


def list_to_dict():
    dict_list = get_dict_list()
    dictionary = {}
    for item in dict_list:
        dictionary[item[1]] = item[0]
    return dictionary


def print_dict():
    dictionary = list_to_dict()
    for k, v in dictionary.items():
        print("{} : {}".format(k, v))


if __name__ == "__main__":
    print_dict()
