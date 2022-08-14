N = int(input())


#벌집의 개수는 1칸마다 6 12 18 24 즉, 6의 배수로 늘어남
#1/7/19/37/61

#(N-1)을 6으로 나눈 몫이 1이면 2개 2,3이면 3개 4,5,6이면 4개 7,8,9,10 이면 5개
#단 나머지가 0인 경우 즉 배수는 예외로처리

#끝이 정해져있지 않으므로 반복문 사용


line=0

for i in range(2,1000000,1):
    number = (N-1)//6
    if (N-1)%6==0:
        number=number-1


    #1~7의 경우는 따로 예외를 두어서 처리함
    if N == 1:
        print(1)
        break
    if number == 0:
        print(2)
        break


    # 8 즉 3칸의 경우부터는 6의 배수 규칙으로 조건문을 만듬
    #0~6  6~18  18~36 이런 식으로
    if (line)//6<number<=(line+i*6)//6:
        print(i+1)
        break
    line = line + i*6
    


