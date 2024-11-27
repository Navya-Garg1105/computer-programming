# Check if Two Tuples are Equal
# Take two tuples from the user and check if they are equal.
tuple1 = tuple(input("Enter first tuple values separated by commas: ").split(','))
tuple2 = tuple(input("Enter second tuple values separated by commas: ").split(','))

if tuple1 == tuple2:
    print("The tuples are equal.")
else:
    print("The tuples are not equal.")
