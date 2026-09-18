def find_min_drops(floors: int) -> int:
    covered_floors = 0

    for drops in range(1, floors + 1):
        covered_floors += drops
        if covered_floors >= floors:
            return drops


if __name__ == "__main__":
    floors = 100
    answer = find_min_drops(floors)

    print("Number of floors:", floors)
    print("Minimum number of drops:", answer)
