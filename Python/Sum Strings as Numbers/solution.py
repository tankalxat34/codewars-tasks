
def sum_strings(x: str, y: str) -> str:
    """
    1
    62
    49
    --
   111
    
    """
    print(x, y)

    if not x: return "0"
    if not y: return "0"

    result = str()


    a, b = "0" * (len(x) - len(y)) + y, "0" * (len(y) - len(x)) + x

    print(a, b)

    in_mind = "0"
    for i in range(1, len(a) + 1):
        summ = int(in_mind) + int(a[-i]) + int(b[-i])

        if summ > 9:
            print(i, len(a), summ)
            if not (i == len(a)):
                in_mind = str(summ)[0]
                result += str(summ)[1]
            else:
                in_mind = "0"
                result += str(summ)[::-1]
        else:
            in_mind = "0"
            result += str(summ)


    return result[::-1]



if __name__ == "__main__":
    print(sum_strings("00103", "08567"))