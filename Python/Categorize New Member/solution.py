"""
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

"""

def open_or_senior(data: list) -> list:
    result = []
    for player in data:
        age, skill = player
        if age >= 55 and skill > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result


if __name__ == "__main__":
    print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))