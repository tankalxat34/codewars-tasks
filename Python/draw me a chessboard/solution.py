
def chess_board(rows, columns):
    s = "XO"
    result = []
    for r in range(rows):
        result.append([])
        s = s[::-1]
        for c in range(columns):
            result[r].append(s[c % 2])
    return result


def chess_board2(rows, columns):
    s = "XO"
    return [[s[c % 2] for c in range(columns)] for r in range(rows)]

if __name__ == "__main__":
    print(chess_board2(6, 4))
    # print(chess_board(3, 7))
