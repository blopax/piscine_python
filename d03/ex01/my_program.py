import local_lib.path as path

if __name__ == "__main__":
    try:
        path.os.makedirs('folder', exist_ok=True)
        with open('./folder/file.txt', 'a+') as fd:
            fd.write("BOOM\n")
        with open('./folder/file.txt', 'r+') as fd:
            string = fd.read()
        print(string, end='')
    except (ModuleNotFoundError, NameError, IOError, EnvironmentError):
        print("An issue occured with the program.")
