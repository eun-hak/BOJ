
#시험 과목의 개수 N을 입력받음
N=int(input())


#그 후 현재 성적을 입력받기 위해 split함수로 공백에 따라 숫자를 입력받음
#그 후 map함수로 int처리

M= list(map(int,input().split()))

#합계를 저장하기 위해 Sum 변수 지정
Sum= 0

#반복문 안에 리스트를 넣어 각 숫자마다 리스트의 최대값을 나누고 100을 곱한 후
#Sum변수에 저장

for j in M:

        Sum= Sum+j/max(M)*100


#그 후 평균을 구하는 값을 프린트함
print(Sum/len(M))




