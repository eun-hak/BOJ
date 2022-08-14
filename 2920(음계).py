
#ascending을 리스트에 저장
b=[1, 2, 3, 4, 5, 6, 7, 8]
#descending을 리스트에 저장
c=[8, 7, 6, 5, 4, 3, 2, 1]


#입력받을 숫자를 리스트에 저장
a= list(map(int,input().split()))


#if elif else문으로 구별 후에 출력
if a ==b:
    print("ascending")
elif a ==c:
    print("descending")
else:
    print("mixed")
    
