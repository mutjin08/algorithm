n, m = map(int, input().split())
ss = []
for _ in range(n):
    ss.append(input())

cnt = 0
for _ in range(m):
    target = input()
    flag = 0
    for s in ss:
        if target in s:
            flag = 1
            break
    cnt += flag

print(cnt)