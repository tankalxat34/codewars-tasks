
def narcissistic(value: int) -> bool:
    n_str = str(value)

    amount = 0
    for s in n_str:
        amount += int(s) ** len(n_str)
    return amount == value


if __name__ == "__main__":
    print(narcissistic(153))
    print(narcissistic(1652))
    print(narcissistic(1927890457142960697580636236639))
    print(narcissistic(12679937780272278566303885594196922))
