def remove_item_by_index(arr, index):
    if 0 <= index < len(arr):
        arr.pop(index)


my_array = [1, 2, 3, 4, 5]
index_to_remove = 2
remove_item_by_index(my_array, index_to_remove)
print(my_array)
