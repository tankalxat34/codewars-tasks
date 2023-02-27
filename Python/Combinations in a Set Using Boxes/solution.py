def combs_non_empty_boxes(n: int, k: int) -> int:
    if (k > n):
        return "It cannot be possible!"
    else:
        results = []
        boxes = []
        balls = list(range(1, n + 1))
        # print(balls)
        # print(boxes)
        # for box_index in range(k):
        ball_index = 1
        box_index = 0
        for index in range(k):
            # print(balls[index:])
            # boxes.append([balls[index:][0]])
            boxes.append([balls.pop(0)])
            box_index += 1
            print(index)
        
        for i in range(k):
            boxes[i] = [*boxes[i], balls[0]]
                        

        print(f"{balls = }")
        print(f"{boxes = }")

            


# n: amount of elements of the sets
# k: amount of equal boxes
# combs: amount of combinations of elements with non empty boxes

if __name__ == "__main__":
    print(combs_non_empty_boxes(4, 3))