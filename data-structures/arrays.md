# Arraysa

An array is a data structure that stores a fixed-size sequence of elements of the same type. In Python, arrays can be created using the built-in `array` module. However, the more commonly used data structure for storing sequences of elements in Python is the `list`.

A list in Python can be considered as a dynamic array, as its size can change dynamically as elements are added or removed. Here's an example of creating and using an array in Python:

```python
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
```

In the above example, `my_array` is a list that stores integers. Elements in the array can be accessed using index notation (`my_array[index]`) and modified as needed. The `append()` method is used to add elements to the end of the array, while the `remove()` method is used to remove elements from the array.