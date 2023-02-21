N = int(input())

array = []
for i in range(N):
    a= input()
    array.append(a)

array = list(set(array))

#1순위 조건이 마지막에 오게끔
array.sort()
array.sort(key=len)


for i in array:
    print(i)
    
