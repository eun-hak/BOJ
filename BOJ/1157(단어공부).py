s =input()

#출력이 대문자로 나오므로 모두 대문자로 바꾼후 리스트에 넣음
S = list(s.upper())
D = list()


#중복 제거한 후 비교를 위해 set함수에 잠깐 들렀다 옴
#set함수는 중복되는걸 알아서 제거함
Set = list(set(S))


#D리스트 안에 S리스트의 단어별 개수를 저장함
for i in Set:
            #a.count() =  a리스트 안에 들어있는 문자의 개수 출력
    D.append(S.count(i))






## 좀 헷갈리는데 D.count(max(D)) 여기서 max(D)가 들어가는 값이 아닌 함수자체로
## 해석이 되는거라고 봐야 되는데 이 경우는 파이썬이 만든 규칙인가?


#만약 가장 최댓값이 2개 이상이면 ? 출력
if D.count(max(D))>1:
    print("?")

else:
    #아니면 D의 최댓값을 인덱스로 가지는 Set의 리스트 값을 출력
    print(Set[D.index(max(D))])
    
    #Set의 인덱스 순서에 따라 그대로 D에 넣었기 때문에 이 과정이 가능
    #Set이 아닌 S에 넣게 된다면 틀림  (세심한 point)
