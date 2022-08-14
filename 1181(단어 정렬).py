a= int(input())

#리스트안에 값을 넣음
#중복제거를 위해 set함수에 넣었다 뺌
#sort()로 낱말순 정렬 후 sort(key=len)으로 길이순 정렬
#for문으로 출력


c=[]

for i in range(a):
    b=input()
    c.append(b)
b=set(c)
c=list(b)
c.sort()
c.sort(key=len)
for i in c:
    print(i)



    
