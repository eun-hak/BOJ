
#1순위 : 5봉지
#2순위 : 3봉지
#->5의 배수가 될때까지 설탕을 3빼주면 됨

sugar = int(input())

a = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  
        a += (sugar // 5)  
        print(a)
        break
    sugar -= 3  
    a += 1  
else :
    print(-1)

'''
num_list=[]
a= N/5
b= N/3
c= N//5 + (N%5)/3
d= N//3 + (N%3)/5
e=-1
num_list.append(e)

if N%5==0:
    num_list.append(a)
if N%3==0:
    num_list.append(b)
if ((N%5)%3)==0:
    num_list.append(c)
if ((N%3)%5)==0:
    num_list.append(d)
num_list.sort()
print(num_list)
if len(num_list)>1:
    del num_list[0]

list_int = list(map(int,num_list))

print(list_int[0])
'''


