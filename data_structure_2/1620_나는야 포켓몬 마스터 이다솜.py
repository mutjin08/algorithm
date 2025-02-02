import sys
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())

to_idx, to_name = {}, {}
for idx in range(1, n+1):
    name, idx = input(), str(idx)
    to_name[idx], to_idx[name] = name, idx

for _ in range(m):
    target = input()
    
    if target.isalpha():
        print(to_idx[target])
    else:
        print(to_name[target])
