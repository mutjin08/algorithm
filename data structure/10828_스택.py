import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
s = deque([])

for _ in range(n):
    cmd = input().split()
    if len(cmd)>1:
        x = cmd[1]
    cmd = cmd[0]

    if cmd == "push":
        s.append(x)
    elif cmd == "pop":
        if s:
            print(s.pop())
        else:
            print(-1)
    elif cmd == "size":
        print(len(s))
    elif cmd == "empty":
        if not s:
            print(1)
        else:
            print(0)
    elif cmd == "top":
        if s:
            print(s[-1])
        else:
            print(-1)
    else:
        print("wrong input")

