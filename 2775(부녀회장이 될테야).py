T= int(input())
#   3층                 1 5 15 35 70 126 210
#   2층                 1 4 10 20 35 56 84
#   1층                 1 3 6  10 15 21 28 
#   0층                 1 2 3  4  5  6  7

#먼저 0층은 1씩 올라가기 때문에 0층을 기준으로 리스트를 만듬
#그 후 위층은 앞의 숫자를 다 합하도록 for문으로 작성
#층수마다 for문을 반복해야하므로 층수별로 2중 for문을 작성
#마지막으로 출력할 부분은 리스트의 마지막 부분이므로 [-1]




for i in range (T):
    k= int(input())
    n= int(input())

    #리스트 내포
    floor_0=[x for x in range(1,n+1)]
    
    for q in range(k):
        for i in range(1,n):
            floor_0[i] +=floor_0[i-1]
            
                
    print(floor_0[-1])
                
            
            
        


    



