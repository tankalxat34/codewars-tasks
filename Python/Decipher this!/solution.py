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