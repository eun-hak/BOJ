#먼저 숫자 하나하나 리스트안에 넣어야되기때문에 문자로 입력을 받음
#그 후 a리스트에 하나하나 int처리해서 집어넣음
#그 후 a와 반대로된 b리스트를 reversed문을 이용해 작성
#a와 b를 비교하여 출력문 작성

while(True):
    
    T=input()

    if T=="0":
        break
    
    a=[]
    for i in T:
        a.append(int(i))

    b=list(reversed(a))

    

    if a==b:
        print("yes")
    else:
        print("no")
    
    

    
