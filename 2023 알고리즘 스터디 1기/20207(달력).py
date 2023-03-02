n = int(input())
canlender = [0] * 366

for _ in range(n):
    s, e = map(int, input().split(' '))

    for i in range(s, e + 1):
        canlender[i] += 1

row = 0
col = 0
ans = 0
for i in range(366):
    if canlender[i] != 0:           #일정이 1개 이상 있을 때
        row = max(row, canlender[i])
        col += 1
    else:                           #일정이 0개 있을 때
        ans += row * col
        row = 0
        col = 0
ans += row * col
print(ans)
