'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import math


def prod(lst):
    prod = 1
    for i in range(len(lst)):
        prod = prod * lst[i]
    return prod


def list_gcd(lst):
    g = lst[0]
    for i in range(1,len(lst)):
        g = math.gcd(lst[i], g)
    return g


t = int(input())
list = [int(x) for x in input().split(" ")]

g = list_gcd(list)
f = prod(list)

print((f ** g) % ((10 ** 9) + 7))