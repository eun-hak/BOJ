
#우선 빈 리스트를 만듭니다
b=[]
#그 후 서로 다른 나머지의 개수를 10개로 지정합니다
count=10

#이제 입력 받을때마다 42로 나눈 나머지를 빈 리스트에 집어넣습니다
for i in range(10):
    a= int(input())

    c=a%42
    
    b.append(c)
    #만약 입력받은 리스트의 값의 개수가 1이 아니라면
    if not b.count(c)== 1:
    #개수를 1개 줄입니다.   
        count= count-1
    #for문으로 10번 반복하기 때문에 입력 받을때마다 알 수 있습니다


print(count)
