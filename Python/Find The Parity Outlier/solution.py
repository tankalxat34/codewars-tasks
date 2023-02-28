def find_outlier(integers):
    arr = [integers[i] % 2 for i in range(len(integers))]
    return integers[arr.index(1) if arr.count(0) > 1 else arr.index(0)]

if __name__ == "__main__":
    print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
    print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))