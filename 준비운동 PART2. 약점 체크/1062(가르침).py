'''

#acint 즉 5글자이상 아니면 읽을 수 있는 글자는 무조건 0개
import sys
from itertools import combinations
input = sys.stdin.readline

N,K = map(int,input().split())

arr = []
for _ in range(N):
    arr.append(input().rstrip())


new_visited = set([])

sw = True

if K<5:
    sw =False
else:
    K = K-5

# 새단어 넣어주기

for i in range(N):
    arr[i] = arr[i][4:-4]                                   #antiwwtica  => ww 로 바뀌는 과정
    for x in arr[i]:
        if x !='a' and x !='n' and x!='t' and x!='i' and x!='c':
            new_visited.add(x)

new_visited = list(new_visited)

res = 0
#판단 과정


if sw:
    if K> len(new_visited):
        K = len(new_visited)     # 중복 제거


    for comb in combinations(new_visited,K):
        cnt = 0

        for x in arr:
            for y in x:         #글자 하나하나 마다  판별하여 단어를 읽을 수 있는지 없는지 판단
                if y not in comb and y !='a' and y !='n' and y!='t' and y!='i' and y!='c':
                    break
            else:
                cnt+=1


        res = max(res,cnt)

    print(res)
else:
    print(0)
'''




from itertools import combinations 
import sys
n, k = map(int, input().split())
answer = 0
# a,n,t,i,c는 반드시 가르쳐야 함

first_word = {'a','n','t','i','c'}

remain_alphabet = set(chr(i) for i in range(97, 123)) - first_word
data = [sys.stdin.readline().rstrip()[4:-4] for _ in range(n)]

def countReadableWords(data, learned):
   cnt = 0
   for word in data:
      canRead = 1
      for w in word:
          # 안배웠으니까 못읽는다.
         if learned[ord(w)] == 0:
            canRead = 0
            break
      if canRead == 1:
         cnt += 1
   return cnt

if k >= 5:
   learned = [0] * 123
   for x in first_word:
      learned[ord(x)] = 1

   # 남은 알파벳 중에서 k-5개를 선택해본다.
   for teach in list(combinations(remain_alphabet, k-5)):
      for t in teach:
         learned[ord(t)] = 1
      cnt = countReadableWords(data, learned)

      if cnt > answer:
         answer = cnt
      for t in teach:
         learned[ord(t)] = 0
   print(answer)
else:
   print(0)

