import sys
import math
n = int(input())
nums = map(int, sys.stdin.readline().split())
s = sum(nums) + 1
e = math.ceil(s/n)
print(e)