def nb_year(p0, percent, aug, p):
    my_percent = percent / 100 if percent > 1 else percent
    print(my_percent)
    population = p0
    counter = 0
    while population < p:
        population = population + population * my_percent + aug
        counter += 1
        print(population)
    return counter

if __name__ == "__main__":
    # print(nb_year(1000, 2, 50, 1200))
    print(nb_year(1500000, 0.25, 1000, 2000000))