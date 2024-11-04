Write a program to generate the Fibonacci sequence

Program :
n=int(input("Enter n :"))
a=0
b=1
print("Fibonacci series : ")
print(a)
print(b)
i=2
while i<n:
c=a+b
print(c)
a=b
b=c
i+=1

Output :
Enter n :6
Fibonacci series :
0
1
1
2
3
5