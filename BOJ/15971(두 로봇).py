#리스트 컴프리헨션은 최적화의 기본이기 때문에
#나중에 솔루션보고 이해를 빨리 하기 위해서라도 숙지해두는게 좋음



#dfs는 전체노드에 대한 이중리스트와
#방문에 대한 리스트 두개로 이루어져있음
#이중리스트에는 각 인덱스별로 어디노드와 이어져있는지 알려줌





#두 지점사이의 경로가 유일하다 -> 길은 하나이기 때문에
#                                 가장 큰값 한개만 전체에서 빼면 됨


 
import sys
sys.setrecursionlimit(1000000)  #재귀 최대 깊이 생성



def dfs(now,max_length,total):
    if now == end:      
        print(total-max_length)         #경로 도착시 (전체길이- 가장큰 길이 한개) 
        return

    for next,next_length in aisle[now]: #현재 dfs 인덱스에 있는 가지 및 길이를 넣음 
        if not visited[next]:           #방문 되지 않았다면
            visited[next] =True         #방문처리 
            dfs(next,max(max_length,next_length),total+next_length)
                                        # 그 후 가장 큰 가지를 max함수로 설정후
                                        # 최대값에도 추가
                        
    
N,start,end= map(int,input().split())   

aisle = [[] for _ in range(N+1)]        #리스트 컴프리헨션으로 이중리스트 생성
                                        
for i in range(N-1):
    a,b,length = map(int,input().split())
    
    aisle[a].append((b,length))           #해당 노드(인덱스)에 해당하는 가지 및 길이
    aisle[b].append((a,length))           #해당 노드(인덱스)에 해당하는 가지 및 길이


visited =[False]*(N+1)                    #dfs 가지 생성
visited[start] = True                     #첫 가지는 방문처리
dfs(start,0,0)











