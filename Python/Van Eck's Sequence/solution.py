
def seq1(n):
    r = [0]
    last_indexes = dict()
    for i in range(1, n):
        if r[i - 1] in last_indexes:
            r.append(i - 1 - last_indexes[r[i - 1]])
        else:
            r.append(0)
        last_indexes[r[i - 1]] = i - 1
    return r


def find(arr: list, term: int) -> int:
    m_i = 0
    for i in range(len(arr)):
        if arr[i] == term and i > m_i:
            m_i = i

    return m_i

def seq2(n):
    r = [0]
    for i in range(1, n):
        if r[i - 1] in r[:-1]:
            r.append(i - 1 - find(r[:-1], r[i - 1]))
        else:
            r.append(0)
    return r


def seq(n):
    r = [0]
    for i in range(1, n):
        if r[i - 1] in r[:-1]:
            r.append(i - 1 - find(r[:-1], r[i - 1]))
        else:
            r.append(0)
    return r[-1]



if __name__ == "__main__":
    # print(seq2(20))
    print(seq(0))
    # print(find([0, 0, 1, 0, 2, 0, 2], 1))
