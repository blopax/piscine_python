def get_dict():
    d = {
        'Hendrix': '1942',
        'Allman': '1946',
        'King': '1925',
        'Clapton': '1945',
        'Johnson': '1911',
        'Berry': '1926',
        'Vaughan': '1954',
        'Cooder': '1947',
        'Page': '1944',
        'Richards': '1943',
        'Hammett': '1962',
        'Cobain': '1967',
        'Garcia': '1942',
        'Beck': '1944',
        'Santana': '1947',
        'Ramone': '1948',
        'White': '1975',
        'Frusciante': '1970',
        'Thompson': '1949',
        'Burton': '1939',
    }
    return d


def sort_dict():
    d = get_dict()
    raw_list = []
    for k, v in d.items():
        raw_list.append([k, v])
    sorted_list_by_name = sorted(raw_list, key=lambda x: x[0])
    sorted_list = sorted(sorted_list_by_name, key=lambda x: x[1])
    for item in sorted_list:
        print(item[0])


if __name__ == "__main__":
    sort_dict()
