

from itertools import permutations


num = list(permutations(['1','2','3','4','5','6','7','8','9'],3))

N = int(input())

removeCount = 0
for _ in range(N):
    test, a, b = list(map(int,input().split()))
    test = list(str(test))   ####이렇게하면 숫자를 문자로 인덱싱 가능###
    

    removeCount = 0         #여기도 초기화 시켜줘야됨
    for i in range(len(num)):
        strike = ball = 0   #반복문 돌릴때 마다 strike ball 초기화
        i -= removeCount    #여기가 이제 빼주는곳


                            #여기는 이제 평범한 숫자야구 공식
        for j in range(3):
            if test[j] == num[i][j]:        #리스트랑 완벽히 일치하면 strike
                strike +=1
            elif test[j] in num[i]:      #리스트안에 들어있으면 ball
                ball +=1



        if (strike!= a) or (ball !=b):
            num.remove(num[i])
            removeCount+=1  # 만약 주어진 a b와 다르면 주어진 리스트 인덱스 삭제해야 되는데
                            # 그러면 리스트 다음 인덱스로 넘어가므로 이 값만큼 빼줘서 돌아가야됨


print(len(num))



