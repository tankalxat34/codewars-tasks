import re

def printer_error(s):
    return f'{len(s) - len(re.findall(r"[aA-mM]", s))}/{len(s)}'


if __name__ == "__main__":
    print(printer_error("aaabbbbhaijjjm"))
    print(printer_error("aaaxbbbbyyhwawiwjjjwwm"))