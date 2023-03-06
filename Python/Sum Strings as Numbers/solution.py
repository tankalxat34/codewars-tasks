
def sum_strings(x: str, y: str) -> str:
    """
    1235213572135974534 + 623242142134325
    
    111   <-- in mind  
    9999
    0001
    ----
   10000

      1    
    1239
    0005
    ----
    1244      

    """
    result = str()

    a, b = "0" * (len(x) - 1) + y, "0" * (len(y) - 1) + x

    print(a, b)

    in_mind = 0

    for i in range(1, len(a) + 1):
        local_a, local_b = int(a[-i]) + int(in_mind), int(b[-i])
        
        in_mind = str(local_a + local_b)[0]
        
        print(f"{i = }", f"{in_mind}")

        try:
            result += str(local_a + local_b)[1]
        except IndexError:
            result += in_mind

    return result[::-1]



if __name__ == "__main__":
    print(sum_strings('5', '1239')) # 1244
    # print(sum_strings('9999', '5')) # 1244
    # print(sum_strings('1', '1')) # 1244
    # print(sum_strings('1234', '2')) # 3

