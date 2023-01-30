n = int(input())
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input())))


#상하좌우 입력
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]




def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:            #만약 그래프가 1이면
        global count                #전체 개수 1 증가시키고
        count += 1
        graph[x][y] = 0             # 방문 처리 (0)
        for i in range(4):          # 상하좌우 다 살펴봄
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True                 # 다 돌은 후 True 처리
    return False



count = 0
result = 0

for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:       #출발점을 기준으로 하나의 덩어리가 True 처리됨
            num.append(count)
            result += 1             #그리고 그걸 전체 개수로 1개 추가
            count = 0               #다음을 위해 카운트 초기화 



num.sort()
print(result)
for i in range(len(num)):
    print(num[i])
