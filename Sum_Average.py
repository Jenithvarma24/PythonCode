#   To calculate the sum and average of n integer numbers
n = int(input("Enter the number of integers: "))
numbers = [int(input("Enter an integer: "))
           for _ in range(5)]

total = sum(numbers)
average = total / n

print("Sum:", total)
print("Average:", average)