import math

def square_digits(num: int) -> int:
    return int("".join(str(int(math.pow(int(s), 2))) for s in str(num)))

if __name__ == "__main__":
    print(square_digits(9119))