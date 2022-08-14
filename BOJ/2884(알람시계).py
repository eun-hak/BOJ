
#입력으로 띄어쓰기 없이 2개의 숫자를 받으므로
#split()함수로 공백을 기준으로 나눠야 되며
#input()은 문자를 출력하므로 map함수로 int로 변환
h,m= map(int,input().split())




if m>=45:           #분침이 45분보다 클경우 
        
    fix_m = m-45    #그냥 뺌
    fix_h = h       #이 경우 시침은 그대로 

else:               #분침이 45분보다 작은 경우

    fix_m = m-45+60 #시침에서 60분을 빼와서 분침에 더해줌

    if h==0:        #근데 시침이 0시라면 24에서 1을 뺌
        fix_h = 24-1
    else:
        fix_h = h-1


print(fix_h,fix_m)

        
    
