import math

def is_prime(n):
    """
    Returns True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True



if __name__ == "__main__":
    print(is_prime(1))
    print(is_prime(2))
    print(is_prime(11))
    # print(is_prime(75))