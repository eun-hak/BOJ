
#먼저 숫자를 저장할 리스트 두개를 만듭니다
a=list()
b=list()

#그 후 숫자 두개를 입력받는 함수를 작성합니다
A,B = map(int,input().split())


#두 함수는 문자로 바꾸어서 각각의 리스트에 추가합니다
#for문에 문자를 넣기때문에 리스트에는 한문자씩 저장됩니다
for i in str(A):
    a.append(i)

    #['4','3','7']

for j in str(B):
    b.append(j)

    #['3','9','8']
    

#이제 list의 내용을 reverse메서드로 뒤집습니다
a.reverse()
b.reverse()



#그 후 리스트의 숫자를 비교하여 더 큰 숫자의 값을 출력합니다
#for문으로 받기때문에 출력시에 줄바꿈처리를 안하게 end=""를 입력합니다
if a>b:
    
    for k in a:
        print(k,end="")
else:
    
    for p in b:
        print(p,end="")
    
