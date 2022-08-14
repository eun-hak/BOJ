#모든 함수나 변수에 그에 걸맞는 용어를 써줘야 헷갈리지 않음
import sys
input = sys.stdin.readline          #시간초과 문제 해결



#최고등수와 최하 등수를 이중리스트로 만들어서 각 인덱스를
#등수로 취급시킨 후 dfs 돌리는 알고리즘



def dfs(num , Rank_arr):                    #매개변수는 등수와 랭크배열
    count = 1
    
    visited[num] = True
    for NextNum in Rank_arr[num]:           #랭크배열에 있는 첫 인덱스가 등수임
        
        if not visited[NextNum]:
            count +=dfs(NextNum,Rank_arr)   # 그 등수 배열에 들어 있는 두번 째 리스트가 
                                            # 해당 번호가 이길 수 있는 숫자라는 뜻
    return count



N,M,X = map(int,input().split())
Max = [[]for _ in range(N+1)]
Min = [[]for _ in range(N+1)]
visited = [False]*(N+1)                     #dfs 방문 노드 생성
Max_Rank = 1
Min_Rank = N

for i in range(1,M+1):

    A,B = map(int,input().split())

    Max[B].append(A)                #자기가 이기는 등수를 리스트에 넣음
    Min[A].append(B)                #자기가 지는 등수를 리스트에 넣음


Max_Rank += dfs(X,Max)-1            #1을 빼는 이유는 자기 자신의 등수를 포함하기 때문
Min_Rank -= dfs (X,Min)-1

print(Max_Rank , Min_Rank)

