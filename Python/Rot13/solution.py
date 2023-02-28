ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = ascii_lowercase.upper()
 

def rot13(message):
    result = str()
    for s in message:
        if s.lower() == s.upper():
            result += s
        else:
            index = ascii_lowercase.index(s.lower()) + 13
            if index >= len(ascii_lowercase):
                index = abs(len(ascii_lowercase) - index)
            
            if s in ascii_lowercase: result += ascii_lowercase[index]
            if s in ascii_uppercase: result += ascii_uppercase[index]

    return result


if __name__ == "__main__":
    print(rot13("test"))
    print(rot13("Test"))
    print(rot13("aA bB zZ 1234 *!?%"))
    print(rot13("abcdefghijklmnopqrstuvwxyz"))