def create_dict(keys, values):
    result = dict()
    for i in range(len(keys)):
        try:
            result[keys[i]] = values[i]
        except IndexError:
            result[keys[i]] = None
    return result



if __name__ == "__main__":
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    print(create_dict(keys, values))   


    keys = ['a', 'b', 'c', 'd']
    values = [1, 2, 3]
    print(create_dict(keys, values))   

    keys = ['a', 'b', 'c']
    values = [1, 2, 3, 4]
    print(create_dict(keys, values))   



