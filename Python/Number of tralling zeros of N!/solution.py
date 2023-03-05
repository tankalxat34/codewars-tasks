import math

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def zeros(n):
    amount = 0
    for k in range(1, int(math.log(n, 5)) + 1):
        amount += int(n // math.pow(5, k))
    return amount


if __name__ == "__main__":
    print(zeros(12))