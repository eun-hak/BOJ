n,k= map(int,input().split())
from collections import deque


MAX = 10**5
dist = [0] * (MAX+1)        #몇번을 시도했는지 담는 리스트


def bfs():
    q= deque()
    q.append(n)
    
    while q:
        x = q.popleft()
        if x ==k:
            print(dist[x])
            break

        for nx in (x-1, x+1 , x*2):
            if 0<= nx <= MAX and not dist[nx]:     #dist[nx]는 처음에 무조건 0이기 때문에 false 반환 (nx라는게 계속 리스트의 첫구간 방문이기 때문에 계속 false 반환)
                dist[nx] = dist[x] +1               #몇번 시도했는지 숫자 세는 기능
                q.append(nx)                        #(첫시도기준)  이제 큐에 deque([4,8,10])이 들어감 


bfs()
