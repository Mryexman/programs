Programs that take command line arguments(word count)

Program:

import sys
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
# Arguments passed
print("\nName of Python script:", sys.argv[0])
print("\nArguments passed:", end = " ")
for i in range(1, n):
print(sys.argv[i], end = " ")
#Addition of numbers
Sum = 0
# Using argparse module
for i in range(1, n):
Sum += int(sys.argv[i])
print("\n\nResult:", Sum)

output :
 python cmd.py 1 2 3 4 5 6
total args passed : 7
name of py script : cmd.py
args passed: 1 2 3 4 5 6
result : 21