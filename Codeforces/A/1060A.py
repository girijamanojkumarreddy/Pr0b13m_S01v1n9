import sys
input=sys.stdin.readline
n=int(input())
s=input()
print(min(s.count('8'),n//11))