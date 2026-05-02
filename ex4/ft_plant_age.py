def ft_plant_age():
    age = input("Enter plant age in days: ")
    if int(age) >= 60:
        print("Plant is ready for harvest!")
    else:
        print("Plant needs more water!")
