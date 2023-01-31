#https://daekyoulibrary.tistory.com/entry/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%84-%ED%86%B5%ED%95%B4-%EA%B5%AC%ED%98%84%ED%95%9C-DFS%EC%99%80-BFS

#참고자료 
from collections import deque
A, B, C = map(int,input().split())

visited = [False] * (A+1)



#graph = [[]]*A   이렇게하면 참조문제 발생   ( 모든 인덱스가 같은 값을 참조함)

graph = [[]for i in range(A+1)]       # 이거 디따 중요   리스트컴프리헨션 참조문제

for i in range(B):
   a,b = map(int,input().split())
   graph[a].append(b)
   graph[b].append(a)
   

#리스트 초기화
for i in range(A+1):
    graph[i].sort()

# dfs 재귀 사용
def dfs(graph,start,visited):
    
    visited[start] = True
    print(start, end =' ')

    #그래프 노드에 있는 인덱스를 뽑아와서 방문되지 않았다면 재귀로 돌림
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i , visited)
    



#bfs 덱 사용
def bfs(graph,start, visited):
    queue = deque([start])
    visited[start] = True

    #큐가 빌때까지 큐안에 원소를 넣고 그 큐와 연결된 방문되지 않은 원소들을 삽임
    while queue:
        v = queue.popleft()
        print(v , end = ' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


        
dfs(graph , C, visited)
print()
visited = [False] * (A+1) # 초기화 해줘야됨
bfs(graph, C, visited)

