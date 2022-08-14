#블랙잭
#입력값을 map함수로 받음
#그 후 카드의 입력값은 리스트에 안에 넣어둠
#숫자는 임의로 주어지기에 sort()함수로 정렬시켜두면 편함
N,M = map(int,input().split())
card = list(map(int,input().split()))
card.sort()

#리스트 내포를 이용하여 각 숫자를 모두 더한 경우의 수를 모두 저장
CARD= [a+b+c for a in card  for b in card for c in card if a!=b and a!=c and b!=c]


#만약 정해진 숫자 M이 리스트안에 있다면 호출
#그렇지 않다면 500을 리스트안에 넣은 후 그 앞에 인덱스를 호출하면 됨
if M in CARD:
    print(M)
else:
    CARD.append(M)
    CARD.sort()
    find_CARD=CARD.index(M)
    print(CARD[find_CARD-1])
    
    
    
