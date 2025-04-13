# time over
import sys
input = sys.stdin.readline

from collections import deque

n = int(input())

q = deque([])

for _ in range(n):
    cmd = input().split()
    if len(cmd)>1:
        x = cmd[1]
    cmd = cmd[0]

    if cmd == "push":
        q.append(x)
    elif cmd == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif cmd == "size":
        print(len(q))
    elif cmd == "empty":
        if not q:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd == "back":
        if q:
            print(q[-1])
        else:
            print(-1)
    else:
        print("wrong input")

