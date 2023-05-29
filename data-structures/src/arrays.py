my_array = [1, 2, 3, 4, 5]  # Creating an array with initial elements

# Accessing elements in the array
print(my_array[0])  # Output: 1
print(my_array[2])  # Output: 3

# Modifying elements in the array
my_array[3] = 10
print(my_array)  # Output: [1, 2, 3, 10, 5]

# Adding elements to the array
my_array.append(6)
print(my_array)  # Output: [1, 2, 3, 10, 5, 6]

# Removing elements from the array
my_array.remove(3)
print(my_array)  # Output: [1, 2, 10, 5, 6]

my_list = []  # Creating an empty list

# Adding elements to the list
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list)  # Output: [1, 2, 3]

# Adding more elements to the list
my_list.append(4)
my_list.append(5)
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Removing elements from the list
my_list.remove(3)
print(my_list)  # Output: [1, 2, 4, 5]