<<<<<<< HEAD
def decipher_this(s):
    result = ""
    lst = []
    str_num = ""
    for i, symbol in enumerate(s):
        if symbol in "0123456789":
            str_num += symbol
        else:
            if str_num:
                result += chr(int(str_num))
                str_num = ""

            result += symbol
    
    for word in result.split():
        w = list(word)
        print(w)
        try:
            w[1], w[-1] = w[-1], w[1]
        except IndexError:
            pass
        lst.append("".join(w))
    
    return " ".join(lst)



if __name__ == "__main__":
    print(decipher_this("72olle 103doo 100ya"))
    print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"))
=======
import re

ascii_numbers = "0123456789"

def decipher_this(s):
    result = ""
    words = s.split()
    
    number = ""
    cache = ""
    for i, symbol in enumerate(s):
        if symbol in ascii_numbers:
            number += symbol
        else:
            if number != "":
                result += chr(int(number))
                # result.append(chr(int(number)))
                number = ""
            if symbol == " ":
                pass

                
            result += symbol



    print(result)
        

if __name__ == "__main__":
    print(decipher_this("72olle 103doo 100ya"))
>>>>>>> 91ca40a4e11cd772ffbe1eac68ca5c892a1c30b0
