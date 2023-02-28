import math

def dig_pow(n, p):
    n_str = str(n)

    amount = 0
    pow_counter = p

    for s in n_str:
        amount += int(math.pow(int(s), pow_counter))
        pow_counter += 1

    if (amount % n == 0):
        return amount // n
    else:
        return -1


if __name__ == "__main__":
    print(dig_pow(89, 1))
    print(dig_pow(92, 1))
    print(dig_pow(46288, 3))
    print(dig_pow(46288, 5))