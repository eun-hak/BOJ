
money = int(input())           #입력받을 돈

money_list = [5,2]             # 5원과 2원을 리스트에 등록
 
money_list_num= 0              # 동전 전체 개수 저장


while money != 0:

    if money ==1:
         money_list_num = -1
         break
    elif money % money_list[0] == 0:            #moeny_list[0] = 5를 의미
        money_list_num += money // money_list[0]            #5로 나눠떨어지면 그대로 개수 세면 됨
        break
    else:                                                   # 그렇지 않다면 2를 빼고 다시 진행
        money -=money_list[1]
        money_list_num+=1

 

print(money_list_num)







