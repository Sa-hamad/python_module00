def ft_seed_inventory(s_t: str, q: int, u: str) -> None:

    if (str(u) == "packets"):
        print(s_t.capitalize(), "seeds:", int(q), str(u), "available")
    elif (str(u) == "grams"):
        print(s_t.capitalize(), "seeds:", int(q), str(u), "total")
    elif (str(u) == "area"):
        print(s_t.capitalize(), "seeds: covers",
              int(q), str(u), "square meters")
    elif (str(u) == "unknown"):
        print("Unknown unit type")
