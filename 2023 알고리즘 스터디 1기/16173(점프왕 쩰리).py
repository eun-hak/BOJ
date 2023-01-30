#BFS 를 사용할 때 파이썬에서
#큐를 list 타입을 사용해 자료를 입력할 때는 list.append(something),
#출력할 때는 list.pop(0) 와 같이 구현하시는 분들이 있는데,
#이는 시간복잡도가 O(N)이라 시간적으로 매우 비효율적임
#그러므로 collections 라이브러리의 deque를 사용하면 시간을 절약 가능




from collections import deque



def bfs(x,y,visited):
    
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    
    #큐가 비어있을 때 까지
    # 파이썬에서는 자료형이 비어있으면 Flase 채워져있으면 True를 반환
    while queue:
        x,y = queue.popleft()
        #-1 지점까지 계속 탐색을 진행함
        if array[x][y] ==-1:
            return 'HaruHaru'


        for i in range(2):
            #오른쪽 + 아래를 탐색하기 위함
            nx = x + dx[i] * array[x][y]
            ny = y + dy[i] * array[x][y]
 
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            #만약 방문했다면 무시하고 다음걸로
            if visited[nx][ny] == True:
                continue
            #아니면 방문 처리하고 큐에 넣음
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny))
    return 'Hing'


 
n = int(input())
array = [list(map(int,input().split())) for i in range(n)]
visited = []
for i in range(n):
    visited.append([False]*n)
#리스트 컴프리헨션으로 간소화




#아래랑 오른쪽을 계속 돌아야 하므로 설정
dx = [1,0]
dy = [0,1]


 
print(bfs(0, 0, visited))





        

