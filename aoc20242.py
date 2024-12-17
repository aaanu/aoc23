def is_increasing(numbers):
  """Checks if a list of numbers is strictly increasing."""
  return all(numbers[i] < numbers[i+1] for i in range(len(numbers)-1))

def is_decreasing(numbers):
  """Checks if a list of numbers is strictly decreasing."""
  return all(numbers[i] > numbers[i+1] for i in range(len(numbers)-1))

def is_safe(l: list[int]) -> bool:
    increasing = is_increasing(l)
    decreasing = is_decreasing(l)
    if not increasing and not decreasing:
       return False
    return all(abs(l[i] - l[i+1]) < 4 and abs(l[i] - l[i+1]) > 0 for i in range(len(l) - 1))

def can_be_safe(l: list[int]) -> bool:
    for i in range(len(l)):
        # Create a sublist with the current number removed
        sublist = l[:i] + l[i+1:]

        # Check the condition
        condition_satisfied = is_safe(sublist)
        if condition_satisfied:
           return True
    return False

with open('./Downloads/input.txt', 'r') as input:
    data = input.readlines()
    safe_count = 0
    safe_lists = []
    for index, line in enumerate(data):
        numbers = [int(s) for s in line.split(" ")] # looks like [3, 6, 7, 9, 11, 8]
        if is_safe(numbers):
            safe_count += 1
        # comment out below - this is for part 2
        elif can_be_safe(numbers):
           safe_count += 1
    print(safe_count)
    
