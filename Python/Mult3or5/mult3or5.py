
def solution(number):
    if number < 0:
        return 0
    
    arr = list()
    for i in range(1, number):
        if i % 5 == 0 or i % 3 == 0:
            arr.append(i)
    return sum(arr)

if __name__ == "__main__":
    print(solution(10))