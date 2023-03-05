
import sys
from collections import Counter

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))
 
# 산술평균 
one =(round(sum(li)/n))
 
# 중앙값 
li.sort()
two =(li[n//2])
 
# 최빈값
cnt_li = Counter(li).most_common()                 # cnt => (a,b)    a => 가장 많이나온 값     b => 그 개수
if len(cnt_li) > 1 and cnt_li[0][1]==cnt_li[1][1]: #최빈값 2개 이상 => 어차피 처음 2개만 같으면 해당되는거임
    three =(cnt_li[1][0])
else:
    three =(cnt_li[0][0])
 
# 범위
four =(max(li)-min(li))


print(one)
print(two)
print(three)
print(four)
