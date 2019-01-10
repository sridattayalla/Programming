import sys

N, R = map(int, sys.stdin.readline().split())
for _ in range(N):
    r = int(input())
    if(r<R):
        print("Bad boi")
    else:
        print("Good boi")