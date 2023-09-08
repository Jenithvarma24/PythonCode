def find_longest_word(word_list):
    # Check if the list is empty
    if not word_list:
        return None, 0

    # Initialize variables to store the longest word and its length
    longest_word = ""
    max_length = 0

    # Iterate through the words in the list
    for word in word_list:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)

            return longest_word, max_length


word_list = ["jenith", "Ram", "Sam", "Valar", "Bairavi"]
longest_word, length = find_longest_word(word_list)

if longest_word:
    print(f"The longest word is {longest_word} with a length of {length} characters.")
else:
    print("The list is empty.")
