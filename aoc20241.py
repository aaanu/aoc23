import bisect

with open('./Downloads/input.txt', 'r') as input:
    data = input.readlines()
    left = []
    right = []
    diff = 0
    for line in data:
        leftVal, rightVal = line.split("   ", 1)
        bisect.insort(left, int(leftVal))
        bisect.insort(right, int(rightVal))
    assert len(left) == len(right)
    for i in range(len(left)):
        diff_point = abs(left[i] - right[i])
        diff += diff_point
    print(diff)
    # part 2
    similarity_score = 0
    for i in range(len(left)):
        element = left[i]
        appearances = right.count(element)
        if appearances > 0:
            similarity_score += element * appearances
    print(similarity_score)
        
