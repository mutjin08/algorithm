def is_vps(cmd):
    s = 0

    for c in cmd:
        if c == "(":
            s += 1
        else:
            if s > 0:
                s -= 1
            else:
                return "NO"
    
    if s == 0:
        return "YES"
    else:
        return "NO"


t = int(input())
for _ in range(t):
    print(is_vps(input()))