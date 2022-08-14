'''
while(True):
    a,b,c=map(int,input().split())
    if  a==0 and b==0 and c==0:
        break

    elif a>b and a>c and b+c>a:
        if a*a == b*b+c*c:
            print("right")
        else:
            print("wrong")
    elif b>a and b>c and a+c>b:
        if b*b == a*a+c+c:
            print("right")
        else:
            print("wrong")
    elif c>a and c>b and a+b>c:
        if c*c == a*a+b*b:
            print("right")
        else:
            print("wrong")
    else:
        print("wrong")
'''




'''
틀린 이유를 잘 모르겠음
while(True):
    a=list(map(int,input().split()))

    if sum(a) == 0:
        break
    
    sorted(a)
    if a[0]**2 + a[1]**2 ==a[2]**2:
        print("right")
    else:
        print("wrong")
        
'''

while True:
    #리스트에 입력값 3개 저장
    a= list(map(int,input().split()))
    #최댓값 설정
    max_num = max(a)
    # 입력값이 모두 0이면 종료 되므로 합이 0 이면 종료
    if sum(a) ==0:
        break
    #최대값은 리스트에서 빼둠
    a.remove(max_num)
    #직각삼각형 조건 a**2+b**2 == c**2을 이용
    if a[0]**2 + a[1]**2 == max_num**2:
        print('right')
    else:
        print('wrong')

