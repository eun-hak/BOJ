#ACM호텔
#규칙성 파악문제
#예제에 N H 배수에 관한 예시가 없어서 어려움

n = int(input())
for i in range (n):
	
    H,W,N =map(int,input().split())
    #층 수는 앞 번호니까 front
    #방 번호는 뒷 번호니까 back으로 설정

    #만약 층수보다 사람수가 적다면 방번호는 1로 유지 될것이고
    #층 수는 사람수가 될것임
    if N<=H:
        front = N
        back = 1
    #층수가 사람수보다 많으면 층 수는 사람수에서 층수를 나눈 나머지가 되고
    #방번호는 사람 수에서 층수를 나눈것에 1을 더하면 됨
    elif N>H:
        front = N%H
        back=N//H+1
    #만약 사람 수가 층 수의 배수가 되면
    #front 의 나머지가 0이 되고 back 누난 것도 1이 나오므로
    #이 경우만 따로 바꿔야됨

    if N%H == 0:
        front = H
        back = N//H
        
    print(front*100+back)
        
'''
t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    num = n//h + 1
    floor = n % h
    if n % h == 0:  # h의 배수이면,
        num = n//h
        floor = h
    print(f'{floor*100+num}')
'''
