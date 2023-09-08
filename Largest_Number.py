# program to find the largest number in a list
def find_largest(numbers):
    return max(numbers)


numbers = [int(x) for x in input("Enter integers separated by spaces: ").split()]
largest = find_largest(numbers)

print("The largest number is:", largest)