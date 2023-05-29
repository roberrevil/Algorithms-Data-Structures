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