def my_var():
    var_1 = 42
    var_2 = "42"
    var_3 = "quarante-deux"
    var_4 = 42.0
    var_5 = True
    var_6 = [42]
    var_7 = {42: 42}
    var_8 = (42,)
    var_9 = set()
    var_list = [var_1, var_2, var_3, var_4, var_5, var_6, var_7, var_8, var_9]
    for var_i in var_list:
        print("{} est de type {}".format(var_i, type(var_i)))


if __name__ == "__main__":
    my_var()
