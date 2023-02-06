from itertools import permutations
#조합을 이용하여 해결

a= []
for i in range(9):
    N= int(input())
    a.append(N)
total = sum(a)
#입력값 설정



#조합으로 나올 수 있는 모든 경우의 수 판단
List = list(permutations(a,2))


#for문을 통해 100이 나올때까지 조합을 돌림
for i in range(len(List)):
    if total - sum(List[i]) == 100:
        a.remove(List[i][0])
        a.remove(List[i][1])
        break
    


#나온 조합을 추출
for i in sorted(a):
    print(i)
    




