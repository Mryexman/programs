Write a program to check whether the given number is Armstrong or not

Program

a=int(input("Enter a number :"))
sum=0
temp=a
while a>0:
b=a%10
sum+=(b**3)
a=a//10
if(sum==temp):
print(temp,"is an Armstrong number")
else:
print(temp,"is not an Armstrong number ")

Output :
Enter a number :370
370 is an Armstrong number