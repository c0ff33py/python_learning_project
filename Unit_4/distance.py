distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}


def main():
    for distance in distances.values():
        print(f"the {distance} Au is {convert(distance)} m")


main()


def convert(au):
    return au * 149597870700


convert()
