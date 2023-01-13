
# ---- 입력------ #


N = int(input())
c= []           #케이스를 담는 리스트

for i in range(N):
    a = int(input())
    b = list(map(int,input().split()))
    c.append(b)
    


#---- 출력 ----- #


# 반복문을 뒤로 돌려야됨
# 어차피 가장 큰값이 나오면 그 다음값이 오기 전에 팔아야 되기 떄문에
# 반복문을 뒤로 돌리면서 큰값이 나오기 전까지는 빼고 큰값이 나오면 max를 바꾸는 식

profit = 0
Max = 0
for i in c:
    for j in range (len(i)-1,-1,-1):
        if (i[j] >Max):
            Max = i[j]
        else:
            profit += Max-i[j]
    print(profit)
    profit = 0
    Max =0





    
        
