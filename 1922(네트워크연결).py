#크루스컬 알고리즘 사용


N = int(input())
M = int(input())

arr = []
result = 0
root = [i for i in range(N+1)]

for i in range(M):
    Computer_A,Computer_B, cost = map(int,input().split())
    arr.append([cost,Computer_A,Computer_B])

def findRoot(x):                   #부모(루트)를 찾는 함수
    if root[x] !=x:                #연결될 모든 노드가 가장 작은 1을 부모로 나타내야됨
        root[x] = findRoot(root[x])
    return root[x]



arr.sort()                          #적은 비용부터 차례로 정렬

for cost,Computer_A,Computer_B in arr:
    sRoot = findRoot(Computer_A)
    eRoot = findRoot(Computer_B)

    if sRoot != eRoot:              #사이클이 발생하지 않는 경우
        result += cost              #비용 추가


        if sRoot<eRoot:             #둘중 더 작은 수를 부모로 두기 위해
            root[eRoot] = sRoot
        else:
            root[sRoot] = eRoot
            
        
print(result)






