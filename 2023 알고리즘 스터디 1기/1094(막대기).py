num_list = [64,32,16,8,4,2,1]
N = int(input())

answer = 0
a= 0
for i in num_list:
    
    a += i
    #정답일 경우 지금까지의 모든 a값을 출력
    if a == N:
        answer+=1
        print(answer)
        break
    #정답보다 작을 경우 계속 더해감
    elif a<N:
        answer+=1
        continue
    #정답보다 클 경우 더한걸 도로 뺌
    elif a>N:
        a -= i
        continue
        
        
    
