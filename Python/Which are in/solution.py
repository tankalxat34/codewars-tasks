def in_array(array1, array2):
    selected_strings = []
    for i in range(len(array2)):
        for el in array1:
            if el in array2[i]:
                selected_strings.append(el)
    return list(sorted(set(selected_strings)))


if __name__ == "__main__":
    a1 = ["arp", "live", "strong"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    # a1 = ["arp", "mice", "bull"] 
    # a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

    print(in_array(a1, a2))
