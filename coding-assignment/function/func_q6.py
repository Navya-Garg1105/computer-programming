# Find the Maximum Number in a List
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"The maximum number in the list is {find_max(nums)}.")
