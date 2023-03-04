def tribonacci(signature: list, n: int) -> list:
    result = signature[:n]
    for i in range(3, n):
        result.append(result[i - 3] + result[i - 2] + result[i - 1])
    return result

if __name__ == "__main__":
    print(tribonacci([1, 1, 1], 0))