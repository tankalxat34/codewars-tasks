def nb_year(p0: int, percent: float, aug: int, p: int) -> int:
    my_percent = percent / 100 if percent > 1 else percent
    print(my_percent)
    population = p0
    counter = 0
    while population < p:
        population += int(population * my_percent + aug)
        counter += 1
        print(population)
    return counter

if __name__ == "__main__":
    # print(nb_year(1000, 2, 50, 1200))
    # print(nb_year(1500, 5, 100, 5000))
    # print(nb_year(1500000, 2.5, 10000, 2000000))
    print(nb_year(1500000, 0.25, 1000, 2000000))