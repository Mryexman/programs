Write a program to generate all the prime numbers between 1 and n, where n
is a value supplied by the user.

Program:

n= int(input("Enter n: "))
i = 1
print("The prime numbers between 1 and n are")
while i < n:
if i > 1:
for j in range(2, i):
if (i % j) == 0:
break
else:
print(i)
i += 1

Output :
Enter n: 10
The prime numbers between 1 and n are
2
3
5
7