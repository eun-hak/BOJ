
# 최적의 해 :  회의시간을 합한 값이 최소인 것
# 예제에서는 가장 처음 최적의 해는 1-4
# 맨 처음 0-6과 1-4를 비교해서 1-4가 최적의 해라는 결과가 나옴
# 그 후 1-4와 2-13비교
# 그 후 1-4와 3-5 비교
# 1-4는 최적의 해로 확정
# 4부터 찾음
# 4 없음
# 5-7과 5-9비교
# 5-7과 6-10 비교
# 5-7이 최적의 해로 확정
# 7 찾음
# 7 없음
# 8-11과  8-12 비교
# 8-11이 최적의 해로 확정
# 9없음
# 10없음
# 11없음
# 12-14 최적의 해로 확정



# 풀이법
# 우선 리스트를 빨리 끝나는 순으로 정렬해야 될듯?
# 


#lambda함수
# 함수를 따로 선언하지 않고 lambda식으로 대체함



N = int(input())

meeting_time = []

for i in range(N):
    a,b = map(int,input().split())
    meeting_time.append([a,b])
meeting_time = sorted(meeting_time, key = lambda a : a[0])      # 시작을 기준으로 정렬 한번
meeting_time = sorted(meeting_time, key = lambda a : a[1])      # 끝을 기준으로 정렬 한번

last = 0
total = 0

for i, j in meeting_time:
    if i>= last:                #회의 끝나는 시간과 비교했을 때 크다면 그 회의는 최적의 해
        total +=1
        last = j
print(total)



