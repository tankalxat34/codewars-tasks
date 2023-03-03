def seq(n):
    result = [0, 0]
    increment = 0
    for i in range(2, n + 1):
        if increment == result[i - 2]:
            increment += 1
            result.append(increment)
    return result


if __name__ == "__main__":
    print(seq(5))