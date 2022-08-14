#재귀함수와 백트래킹 

def subsequence(a,b):
    #a는 배열의 인덱스
    #b는 비교할 값
    
    global Top
     

    if a>=N:                #인덱스가 총 개수랑 같아지면
        return              #끝냄


    b +=A[a]                #다음 인덱스를 추가
   
                        
    if b==S:
        Top +=1

    subsequence(a+1,b)      #다음  값을 추가한 뒤로 다른 가지로 갈것인지

    subsequence(a+1,b-A[a]) #현재 값 기준으로 다른 가지로 갈것인지
    

        
Top = 0
N,S = map(int, input().split())
A = list(map(int,input().split()))
subsequence(0,0)

print(Top)



