#graph = [[0 for col in range(b)] for row in range(a)]
#print(graph)


#dfs 런타임 오류..
'''
cnt= 0

def DFS(x,y):
    
    #상하좌우 
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if  (0 <= nx < b) and (0 <= ny < a):
            if graph[ny][nx] ==1:
                graph[ny][nx] == 0
                DFS(nx,ny)
            

a,b = map(int,input().split())

graph =[]
for i in range(a):
    graph.append(list(map(int, input())))



for i in range(b):
    for j in range(a):
        if graph[j][i] == 1:
            DFS(i,j)
            cnt+=1

print(cnt)

'''
#BFS 로 해결....


from collections import deque

n, m = map(int, input().split())
maze = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    maze.append(list(map(int, input())))

queue = deque([(0,0)])

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if maze[nx][ny] == 1:
                queue.append([nx, ny])
                maze[nx][ny] = maze[x][y] + 1

print(maze[n-1][m-1])


