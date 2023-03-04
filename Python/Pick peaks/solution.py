
# def has_borders(index: int, arr: list) -> bool:
#     """
#     Return `True` there are boundaries to the 
#     right and left of the specified index that 
#     are smaller than the number at the specified 
#     index 
#     """
#     has_left = False
#     has_right = False
#     for i in range(len(arr)):
#         print(arr[i])
#         if arr[index] > arr[i] and index > i:
#             has_left = True
#         if arr[index] < arr[i] and index < i:
#             has_right = True
#     # print(has_left, has_right, arr[index])
#     return has_left and has_right


def pick_peaks(arr):
    result = {
        "pos": [],
        "peaks": []
    }
    if not arr: return result

    flag = False
    for i in range(1, len(arr)):
        for j in range(len(arr)):
            flag = arr[i] < arr[j]
            if flag:
                break

        print(arr[i], flag)
        if flag:
            result["peaks"].append(arr[i])
            result["pos"].append(i)
            flag = False

    return result

if __name__ == "__main__":
    # print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]))
    # print(pick_peaks([0, 1, 2, 5, 1, 0]))
    print(pick_peaks([1, 2, 2, 2, 1]))
    # print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]))
    # print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]))
    # print(pick_peaks([1, 2, 2, 2, 1]))