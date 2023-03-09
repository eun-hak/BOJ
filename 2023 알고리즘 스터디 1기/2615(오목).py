
graph = []

for i in range(19):
    a = list(map(int,input().split()))
    graph.append(a)


def bfs(x, y):
    target = graph[x][y] # 바둑알의 색

    # 우/아래/대각선 우 아래/ 대각선 우 위 => 4가지 방향을 탐색
    for k in range(4):
        cnt = 1 # 바둑알 수
        nx = x + dx[k]
        ny = y + dy[k]

        # 반복문을 통해 오목이 되는지 확인
        while 0 <= nx < 19 and 0 <= ny < 19 and graph[nx][ny] == target:
            cnt += 1

            # 오목이라면
            if cnt == 5:
                # 육목 체크
                if 0 <= x - dx[k] < 19 and 0 <= y - dy[k] < 19 and graph[x - dx[k]][y - dy[k]] == target:
                    break
                if 0 <= nx + dx[k] < 19 and 0 <= ny + dy[k] < 19 and graph[nx + dx[k]][ny + dy[k]] == target:
                    break

                # 육목이 아니면 성공한 것으로
                # 바둑알의 색과 위치를 출력 후 종료
                print(target)
                print(x + 1, y + 1)
                exit(0)

            # 이전에 이동했던 방향으로 다시 이동
            nx += dx[k]
            ny += dy[k]

    


dx = [0,1,1,-1]
dy = [1,0,1,1]


for i in range(19):
    for j in range(19):
        if graph[i][j] != 0:
            bfs(i, j)

print(0)
            
