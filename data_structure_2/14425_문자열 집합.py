
n, m = map(int, input().split())

ss = []
for _ in range(n):
    ss.append(input())

answer = 0
for _ in range(m):
    t = input()
    flag = 0
    for s in ss:
        if t == s:
            flag = 1
            break
    answer += flag
print(answer)