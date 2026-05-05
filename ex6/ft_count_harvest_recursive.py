i = 1
days = input("Days until harvest: ")


def ft_count_harvest_recursive():
    global i

    if (i in range(1, (int(days)+1))):
        print("Day", int(i))
        i += 1

        ft_count_harvest_recursive()
    else:
        return print("Harvest time!")
