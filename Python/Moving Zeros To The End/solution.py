def move_zeros(lst):
    return [e for e in lst if e] + [0 for i in range(lst.count(0))]
    # result = []
    # counter_zeros = 0
    # for i in range(len(lst)):
    #     if lst[i] == 0:
    #         counter_zeros += 1
    #     else:
    #         result.append(lst[i])
    
    # result.extend([0 for i in range(counter_zeros)])
    # return result

if __name__ == "__main__":
    print(move_zeros([1, 0, 1, 2, 0, 1, 3])) # returns [1, 1, 2, 1, 3, 0, 0]