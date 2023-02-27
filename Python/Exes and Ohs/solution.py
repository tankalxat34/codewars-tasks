def xo(s: str) -> bool:
    s_lower = s.lower()
    dict_x_o = {"x": 0, "o": 0}
    for symbol in s_lower:
        if (symbol in ["x", "o"]):
            try:
                dict_x_o[symbol] += 1
            except KeyError:
                dict_x_o[symbol] = 0
                dict_x_o[symbol] += 1
    return dict_x_o["x"] == dict_x_o["o"]


def xo2(s):

    exes = 0
    ohs = 0

    for c in s.lower():
        if c == 'x':
            exes += 1
        elif c == 'o':
            ohs += 1

    return exes == ohs


if __name__ == "__main__":
    print(xo2("цуау4а"))
