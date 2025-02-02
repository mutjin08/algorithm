import sys
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())

to_name, to_num = {}, {}
for num in range(1,n+1):
    name = input()
    to_num[name] = num
    to_name[str(num)] = name

for _ in range(m):
    target = input()
    if target.isdigit():
        print(to_name[target])
    else:
        print(to_num[target])

