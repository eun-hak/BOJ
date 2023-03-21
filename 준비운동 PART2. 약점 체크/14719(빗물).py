
N,M = map(int,input().split())

array = list(map(int,input().split()))


count =0

tmp= 0
for i in range(1,M-1):
    left_max = max(array[:i])               #현재 위치에서 가장 큰 왼쪽 블록
    right_max = max(array[i+1:])            #현재 위치에서 가장 큰 오른쪽 블록

    compare = min(left_max , right_max)     # 둘중에 가장 작은 블록

    if array[i] <compare:                   # 그 블록이 곧 빗물의 양임
        count += compare -array[i]

  
print(count)
