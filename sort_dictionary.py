my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}

# Sort by value in ascending order
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Sort by value in descending order
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Ascending order:", sorted_dict_asc)
print("Descending order:", sorted_dict_desc)
