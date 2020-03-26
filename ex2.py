import itertools


def ex2(filename="data/ex2.csv"):
    """ex2
    Args:
        filename (string): Name of csv input file. Defaults to "data/ex2.csv".
    Returns:
        string
    """
    with open(filename, "r") as f:
        data = f.readlines()
        data_format = [int(d.rstrip("\n")) for d in data]
        data_format.pop(0)

    l_without_last = data_format[:-1]
    l_without_first = data_format[1:]

    diff = [b-a for a, b in zip(l_without_last, l_without_first)]

    return str(max([sum(1 for _ in g) for _, g in itertools.groupby(diff)])+1)


if __name__ == "__main__":
    # generate_csv_input_file()
    print(ex2())
