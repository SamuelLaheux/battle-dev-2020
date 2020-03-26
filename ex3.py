import itertools


def ex3(filename="data/ex3.csv"):
    """ex3
    Args:
        filename (string): Name of csv input file. Defaults to "data/ex3.csv".
    Returns:
        string
    """
    with open(filename, "r") as f:
        data = f.readlines()
        lines = [d.rstrip("\n") for d in data]
        lines.pop(0)

    clock = [l.split(' ') for l in lines]

    weekdays = [[] for _ in range(5)]
    for c in clock:
        weekdays[int(c[0]) - 1].append(c[1])

    print(weekdays)
    for ind, d in enumerate(weekdays):
        interval = interval_for_one_day(d)
        if interval:
            return f"{ind+1} {interval}"
        else:
            continue


def interval_for_one_day(day):
    if day:
        vec = [0]*600
        for d in day:
            interv = impossible_interval(d)
            putOnes(vec, interv[0], interv[1])

        nb_of_consecutives = [sum(1 for _ in g) for _, g in itertools.groupby(vec)]

        if vec[0] == 0:
            nb_of_consecutives_free = [elt for idx, elt in enumerate(nb_of_consecutives) if idx % 2 != 1]
            nb_of_consecutives_not_free = [elt for idx, elt in enumerate(nb_of_consecutives) if idx % 2 != 0]
            index_begin_for_not_free = -1
        else:
            nb_of_consecutives_free = [elt for idx, elt in enumerate(nb_of_consecutives) if idx % 2 != 0]
            index_begin_for_not_free = 0

        for ind, n in enumerate(nb_of_consecutives_free):
            if n > 60:
                my_index = ind
                break

        res_free = nb_of_consecutives_free[:my_index+1-1]
        res_not_free = nb_of_consecutives_not_free[:my_index+index_begin_for_not_free+1] if my_index + index_begin_for_not_free>=0 else 0

        begin_free_in_minutes = sum(res_free)+sum(res_not_free) + 1

        return_free_interval = "-".join([begin_minutes_to_clock(b) for b in [begin_free_in_minutes, begin_free_in_minutes + 60]])

    else:
        return_free_interval = '08:00-08:59'
    return return_free_interval


def begin_minutes_to_clock(minute=132, hour_basis=8):
    hour = minute // 60
    new_minutes = minute % 60
    add_zero = '0' if new_minutes < 10 else ''

    return f"{hour_basis + hour}:{add_zero}{new_minutes}"


def clock_to_vect(clock='11:09', hour_basis=8):
    cl = clock.split(":")
    hour = int(cl[0])
    minute = int(cl[1])

    return (hour - hour_basis)*60 + minute


def impossible_interval(clock_interval='11:09-11:28'):
    interval = clock_interval.split("-")

    return [clock_to_vect(inter) for inter in interval]


def putOnes(vec, imin, imax):
    return [vec.insert(i, 1) for i in range(imin, imax)]


if __name__ == "__main__":
    # generate_csv_input_file()
    print(ex3())
