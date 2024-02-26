
n = int(input())
likes = []
dic = {}
for _ in range(n**2):
    likes.append(list(map(int, input().split())))
    dic[likes[-1][0]] = likes[-1][1:]

board = [[0 for _ in range(n)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for like in likes:
    target = like[0]
    cands = []
    for x in range(n):
        for y in range(n):
            if board[x][y] != 0:
                continue
            emptyCount, likeCount = 0, 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if board[nx][ny] == 0:
                        emptyCount += 1
                    if board[nx][ny] in like[1:]:
                        likeCount += 1
            cands.append([likeCount, emptyCount, x, y])
    cands.sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))
    likeCount, emptyCount, x, y = cands[0]
    board[x][y] = target

# 만족도 구하기
answer = 0
for x in range(n):
    for y in range(n):
        target = board[x][y]
        likeCount = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny] in dic[target]:
                    likeCount += 1
        if likeCount > 0:
            answer += 10**(likeCount-1)
print(answer)