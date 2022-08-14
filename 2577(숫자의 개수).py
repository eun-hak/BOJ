

b = list()
d=list()
for i in range(3):
    a= int(input())
    b.append(a)


c=b[0]*b[1]*b[2]
#여기까지 곱한 값 구하는 식


for j in str(c):
    d.append(j)



for k in range (0,10):
    print(d.count(str(k)))

    
    




