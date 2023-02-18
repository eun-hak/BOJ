N = int(input())


#리스트 컴프리헨션으로 입력받아야 참조없이 잘 입력됨
#입력값

arr = [[]for _ in range (N)]
for i in range(N):
    a = input()
    for j in a:
        arr[i].append(j)
answer = 0



#부르트포스로 해결


### 매트릭스를 사용할 때는 항상 for문을 2번 돌리게됨
### 부르트포스같은 경우 for문을 어떻게 돌릴지를 잘 판단하는게 중요

#행과 열을 조사하면서 가장 많이 있는 값 찾기
def check(arr):
    n =len(arr)
    answer = 1

    for i in range(n):
        cnt = 1
        #열에서 가장 많이 있는 cnt 찾기
        for j in range(1,n):
            if arr[i][j] ==arr[i][j-1]:
                cnt+=1
            else:
                cnt =1

            if answer<cnt:
                answer = cnt
        #행에서 가장 많잉 있는 cnt 찾기
        cnt = 1
        for j in range(1,n):
            if arr[j][i] == arr[j-1][i]:
                cnt +=1
            else:
                cnt=1

            if answer<cnt:
                answer = cnt              
    return answer


for i in range(N):
    for j in range(N):
        #열 기준 바꾸기
        if j+1<N:
            #swap 함수입니다
            arr[i][j],arr[i][j+1] = arr[i][j+1] , arr[i][j]
            temp = check(arr)
            if temp>answer:
                answer = temp

            #바꿨으면 다시 돌려 놔야됨
            arr[i][j],arr[i][j+1] = arr[i][j+1] , arr[i][j]
        #행 기준 바꾸기
        if i+1<N:
            #swap 함수입니다
            arr[i][j],arr[i+1][j] = arr[i+1][j] , arr[i][j]
            temp = check(arr)
            if temp>answer:
                answer = temp

            #바꿨으면 다시 돌려 놔야됨
            arr[i][j],arr[i+1][j] = arr[i+1][j] , arr[i][j]



print(answer)
