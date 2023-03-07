"""
The find_pair function takes in a list lst and a target sum target. It initializes an empty dictionary seen, which will be used to store each number in the list along with its index.

The function then loops through each number in the list lst, calculates the difference between the target and the current number, and checks if that difference has already been seen before. If the difference has been seen before, that means we have found a pair of numbers that add up to the target, so we return the indices of those two numbers.

If we loop through the entire list and haven't found a pair that adds up to the target, we return None.

Note that this implementation returns the first pair of numbers that add up to the target in order of appearance, which matches the requirements of the problem statement.

"""


def sum_pairs(lst, target):
    seen = {}
    for i, num in enumerate(lst):
        diff = target - num
        if diff in seen:
            return [lst[seen[diff]], lst[i]]
        seen[num] = i
    return None



if __name__ == "__main__":
    print(sum_pairs([1, -2, 3, 0, -6, 1], -6))