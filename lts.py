Various operations on lists, tuples and sets.

1. List -
Program:

# Create a list
a = [1, 2, 3, 4, 5]
# Print the list
print("Original list:", a)
# Append an element
a.append(6)
print("After append:", a)
# Extend the list
a.extend([8, 9, 10])
print("After extend:", a)
# Insert an element
a.insert(2, 10)
print("After insert:", a)
# Remove an element
a.remove(10)
print("After remove:", a)
# Pop an element
a.pop(2)
print("After pop:", a)
# Sort the list
a.sort()
print("After sort:", a)
# Reverse the list
a.reverse()
print("After reverse:", a)

Output :
Original list: [1, 2, 3, 4, 5]
After append: [1, 2, 3, 4, 5, 6]
After extend: [1, 2, 3, 4, 5, 6, 8, 9, 10]
After insert: [1, 2, 10, 3, 4, 5, 6, 8, 9, 10]
After remove: [1, 2, 3, 4, 5, 6, 8, 9, 10]
After pop: [1, 2, 4, 5, 6, 8, 9, 10]
After sort: [1, 2, 4, 5, 6, 8, 9, 10]
After reverse: [10, 9, 8, 6, 5, 4, 2, 1]

Tuple -
Program :

# Create a tuple
a = (10, 20, 30, 40, 50)
# Print the tuple
print(a)
# Accessing tuple elements
print(a[0]) # First element
print(a[-1]) # Last element
# Tuple slicing
print(a[1:3]) # Slicing from index 1 to 3
# Tuple concatenation
b= (60, 70, 80)
print(a + b)
# Tuple multiplication
print(a * 2)
# Tuple length
print(len(a))
# Tuple membership
print(20 in a)
# Tuple min and max
print(min(a))
print(max(b))

Output :
(10, 20, 30, 40, 50)
10
50
(20, 30)
(10, 20, 30, 40, 50, 60, 70, 80)
(10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
5
True
10
80

Sets
Program :

# Create a set
a = {1, 2, 3, 4, 5}
# Print the set
print(a)
# Add an element
a.add(6)
print(a)
# Remove an element
a.remove(4)
print(a)
# Union of sets
b = {4, 5, 6, 7, 8}
print(a.union(b))
# Intersection of sets
print(a.intersection(b))
# Difference of sets
print(a.difference(b))
# Symmetric difference of sets
print(a.symmetric_difference(b))
# Set length
print(len(a))
# Set membership
print(2 in a)

Output :
{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5, 6}
{1, 2, 3, 5, 6}
{1, 2, 3, 4, 5, 6, 7, 8}
{5, 6}
{1, 2, 3}
{1, 2, 3, 4, 7, 8}
5
True