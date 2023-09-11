def find_missing_number(arr):
    expected_numbers = set(range(10, 21))
    return list(expected_numbers - set(arr))


numbers = [11, 13, 15, 16, 17, 19]
missing = find_missing_number(numbers)
print("Missing number(s):", missing)
