# from random import randint, choice


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
    """
    Args:
        filename (string): Name of csv input file. Defaults to "data/ex1.csv".
    Returns:
        string
    """
    with open(filename, "r") as f:
        data = f.readlines()
        data_format = [d.rstrip("\n") for d in data]

    return data_format


if __name__ == "__main__":
    generate_csv_input_file()
    print(ex1())
