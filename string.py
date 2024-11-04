Write a program to perform various string operations

Program

a="Neelima and Amulya"
# Length of the string
print("Length of the string: ", len(a))
#returns index of the first occurance of the string
print("Index : ",a.index("and"))
#returns the number of occurrences of string
print("Count:", a.count("l"))
#returns index of the first occurance of the string
print("find : ",a.find("and"))
# Upper case
print("Upper case: ", a.upper())
# Lower case
print("Lower case: ", a.lower())
# Capitalize
print("Capitalize: ", a.capitalize())
# Title case
print("Title case: ", a.title())
# Replace a substring
print("String after replacement:", a.replace("Amulya","Soudha"))
# Split the string
print("Split string: ", a.split())
# Concatenate strings
b="Soudhamini"
print("Concatenated string: ", a+b)

Output :
Length of the string: 18
Index : 8
Count: 2
find : 8
Upper case: NEELIMA AND AMULYA
Lower case: neelima and amulya
Capitalize: Neelima and amulya
Title case: Neelima And Amulya
String after replacement: Neelima and Soudha
Split string: ['Neelima', 'and', 'Amulya']
Concatenated string: Neelima and AmulyaSoudhamini