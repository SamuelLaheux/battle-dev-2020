# from random import randint, choice
from collections import Counter

def generate_csv_input_file(filename="data/ex1.csv"):
    """Generates csv input file.
    Args:
        filename (string): Name of csv file to generate. Defaults to "data/ex1.csv".
    Returns:
        Nothing
    """
    with open(filename, "w") as f:
        res = ""
        f.writelines(res)


def ex1(filename="data/ex1.csv"):
    """ex1
    Args:
        filename (string): Name of csv input file. Defaults to "data/ex1.csv".
    Returns:
        string
    """
    with open(filename, "r") as f:
        data = f.readlines()
        data_format = [d.rstrip("\n") for d in data]
        data_format.pop(0)

    dict = Counter(data_format)
    first_two_list = [f[0] for f in sorted(dict.items(), key=lambda item: item[1])[-2:]]
    first_two_list.reverse()
    first_two_string = " ".join(first_two_list)
    return first_two_string


if __name__ == "__main__":
    # generate_csv_input_file()
    print(ex1())
