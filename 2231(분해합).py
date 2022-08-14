a=int(input())
#입력 값과 비교할 result 변수 생성
result=0

#입력값전까지 for문으로 돌려서 비교
for i in range(1,a+1):

    ###중요한 부분###
    #숫자 각 자릿수마다 더해줄 것이기 때문에
    #str로 묶은후 map함수로 int로 바꾼후 리스트에 넣어야만
    # 10이 아닌 1,0으로나옴
    A=list(map(int,str(i)))
    
    #현재 숫자와 숫자의 각 자릿수의 합을 result에 넣음
    result= i +sum(A)

    #만약 그 값이 입력값과 같다면 i를 출력
    if result ==a:
        print(i)
        break

    #만약 for문이 끝날때 까지 입력과 같은 값이 없는 경우 0출력
    if i==a:
        print(0)




'''
b=0
for i in range(1,N+1):
if a-b[0]-b[1]-b[2]==b:

    print(b)
A=list()



if str(b) == str(c)+str(d)+str(e) and int(b+c+d+e) == a:
    print(b)


else:
    print(0)

'''




    
#216 -> 198 + 1 + 9 + 8
#175 -> 164 
#350 -> 342
