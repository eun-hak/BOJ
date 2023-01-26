#재귀 리미트 설
import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    # 상하좌우 확인을 위해 dx, dy 생성
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    # 네 방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < b) and (0 <= ny < a):  # nx:ny ↔ M:N 범위 참고
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0  # 배추가 인접할 때 체커  (중복 방지)
                dfs(nx, ny)



#입력값
                
N = int(input())




for i in range(N):
    a,b,c = map(int,input().split())
    graph = [[0 for col in range(b)] for row in range(a)]       #전체를 0으로 설정
    cnt = 0

    #배추가 있는 곳만 1로 설정
    for j in range(c):
        x,y = map(int,input().split())                      
        graph[x][y] = 1



    # 지렁이가 들어갈 곳 찾
    for x in range(b):
        for y in range(a):
            if graph[y][x] == 1:
                dfs(x, y)
                cnt += 1

    
    print(cnt)







            
