N,K = map(int,input().split())

ANSWER = []
for i in range(1,N+1):
    
    if N%i==0:
        ANSWER.append(i)

    

    
if len(ANSWER) < K:
    print(0)

else:
    print(ANSWER[K-1])

