
def sum_strings(x: str, y: str) -> str:
    result = ""

    _x = "0" * (len(y) - len(x)) + x
    _y = "0" * (len(x) - len(y)) + y

    in_mind = "0"
    for i in range(1, len(_x) + 1):
        local_x, local_y = int(_x[-i]) + int(in_mind), int(_y[-i])
        summ = local_x + local_y

        if summ > 9:
            if i != len(_x):
                in_mind = str(summ)[0]
                result += str(summ)[1]
            else:
                in_mind = str(summ)
                result += in_mind[::-1]
                return result[::-1]
        else:
            in_mind = "0"
            result += str(summ)

    result = result[::-1]

    for i in range(len(result)):
        if result[i] == "0":
            result = result[i + 1:]
        else:
            break

    return result or "0"


if __name__ == "__main__":
    print(sum_strings("00103", "08567"))
    # print(rmzeros("08670"))
    
    # print(sum_strings("123", "456"))