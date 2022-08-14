
#숫자의 개수를 입력받음
N=int(input())

#숫자를 합칠 변수 a 설정
a=0

#입력받을 숫자를 리스트에 저장함
n=list(input())

#그 후 리스트에서 한개씩 꺼내와서 더함
for j in n:
    a=a+int(j)


print(a)
