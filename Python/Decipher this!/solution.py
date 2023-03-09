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