# 1
def count_integer(numbers, integer):
    count = 0
    for num in numbers:
        if num == integer:
            count += 1
    if count == 0:
        return 42
    return count

# Example
print(count_integer([1, 2, 3, 4, 5, 4, 4], 4))
print(count_integer([1, 2, 3, 4, 5], 6))

# 2
def list_func(numbers, integer):
    if integer not in numbers:
        return []
    else:
        numbers[numbers.index(integer)] = 6
        reversed_list = numbers[::-1]
        print(reversed_list)
        return numbers

# Example
numbers = [1, 2, 3, 4, 5, 6]
integer = 3
result = list_func(numbers, integer)
print(result)

# 3
def compare_lists(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2 and element not in common_elements:
            common_elements.append(element)
    return common_elements

# Example
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = compare_lists(list1, list2)
print(common_elements)

list3 = [1, 2, 3]
list4 = [4, 5, 6]
common_elements = compare_lists(list3, list4)
print(common_elements)

# 4
def remove_duplicates(lst):
    return list(set(lst))

# Example
lst = [1, 2, 3, 2, 1, 4, 5, 4]
print(remove_duplicates(lst))

lst = [1, 2, 3, 4, 5]
print(remove_duplicates(lst))

# 5
def dict_func(dictionary):
    type_val = dictionary.get('Type', 'unknown type')
    brand_val = dictionary.get('Brand', 'unknown brand')
    price_val = dictionary.get('Price', 'unknown price')
    print(f"You have a {type_val} from {brand_val} that costs {price_val}.")

    dictionary['OS'] = 'Linux'
    print(dictionary)

    return dictionary

# Example
my_dict = {'Type': 'Laptop', 'Brand': 'Dell', 'Price': 1200}
dict_func(my_dict)

# Example with missing keys
my_dict = {'Type': 'Tablet'}
dict_func(my_dict)