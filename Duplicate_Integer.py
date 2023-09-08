# Print the duplicates from the given integer
def find_duplicates(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)


numbers = [int(x) for x in input("Enter integers separated by spaces: ").split()]
duplicate_list = find_duplicates(numbers)

if duplicate_list:
    print("Duplicate integers:", duplicate_list)
else:
    print("No duplicates found.")

