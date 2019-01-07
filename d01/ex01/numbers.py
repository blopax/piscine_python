def numbers_print(filename):
    string = None
    try:
        with open(filename, 'r') as f:
            string = f.read().strip()
    except IOError:
        print("Error while reading file")
        exit(0)
    numbers_list = string.split(',')
    for number in numbers_list:
        print(number)


if __name__ == "__main__":
    numbers_print("numbers.txt")
