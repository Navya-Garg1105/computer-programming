# Calculate the Sum of Squares of a List
def sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers)

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"The sum of squares of the list is {sum_of_squares(nums)}.")
