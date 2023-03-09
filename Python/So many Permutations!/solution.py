import itertools

def join_tuple(t):
    return "".join(t)

def permutations(s):
    return (list(map(join_tuple, list(itertools.permutations(s, len(s))))))

if __name__ == "__main__":
    print(permutations("ab"))