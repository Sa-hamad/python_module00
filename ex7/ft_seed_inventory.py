def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:

    if (str(unit) == "packets"):
        print (seed_type.capitalize(), "seeds:", int(quantity), str(unit), "available")
    elif (str(unit) == "grams"):
        print (seed_type.capitalize(), "seeds:", int(quantity), str(unit), "total")
    elif (str(unit) == "area"):
        print (seed_type.capitalize(), "seeds: covers", int(quantity), str(unit), "square meters")
    elif (str(unit) == "unknown"):
        print ("Unknown unit type")
