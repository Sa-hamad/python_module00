
def ft_count_harvest_iterative():
    i = 1
    days = input("Days until harvest: ")
    while i in range(int(days) + 1):
        print("Day", int(i))
        i += 1
    print("Harvest time!")
