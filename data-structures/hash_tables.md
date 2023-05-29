# Hash Tables

A hash table, also known as a hash map, is a data structure that provides efficient insertion, deletion, and retrieval of key-value pairs. It uses a technique called hashing to map keys to specific positions in an underlying array.

In Python, hash tables are implemented using the built-in `dict` data type, which provides the dictionary data structure. Here's an example of using a hash table (dictionary) in Python:

```python
# Creating a hash table (dictionary)
hash_table = {}

# Inserting key-value pairs
hash_table['apple'] = 2
hash_table['banana'] = 3
hash_table['orange'] = 1

# Retrieving values by key
print(hash_table['apple'])  # Output: 2
print(hash_table['banana'])  # Output: 3

# Updating values
hash_table['banana'] = 5
print(hash_table['banana'])  # Output: 5

# Deleting a key-value pair
del hash_table['orange']
print(hash_table)  # Output: {'apple': 2, 'banana': 5}
```

In the above example, a hash table (dictionary) is created using curly braces `{}`. Key-value pairs are inserted into the hash table using the assignment operator `=`. Values can be retrieved by using the corresponding key within square brackets `[]`. Updating a value is done by assigning a new value to the key. To delete a key-value pair, the `del` keyword is used.

Hash tables provide fast lookups by using a hash function to map each key to a specific position in the underlying array. The hash function converts the key into an integer value (hash code) that determines the index where the corresponding value is stored. This allows for efficient retrieval and update operations on average, with constant time complexity O(1).

However, collisions can occur when two keys map to the same position in the array. To handle collisions, various techniques like separate chaining or open addressing (e.g., linear probing, quadratic probing) are employed.

Hash tables are commonly used in a wide range of applications due to their efficient key-value pair lookups. They are used in caching mechanisms, symbol tables, databases, and various other scenarios where fast access to data based on a key is required.