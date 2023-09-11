def max_product_pair(numbers):
    max_product = float('-inf')
    result = None

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = numbers[i] * numbers[j]
            if product > max_product:
                max_product = product
                result = (numbers[i], numbers[j])

    return result


number_list = [1, 2, 3, 4, 5]
pair = max_product_pair(number_list)
print("Pair with maximum product:", pair)
