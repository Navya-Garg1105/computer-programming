# Find Prime Numbers in a List
print("Find Prime Numbers in a List")

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

my_list = input("Enter numbers separated by spaces: ").split()
my_list = [int(x) for x in my_list]
primes = [x for x in my_list if is_prime(x)]
print("Prime numbers in the list:")
for x in primes:
    print(x)
