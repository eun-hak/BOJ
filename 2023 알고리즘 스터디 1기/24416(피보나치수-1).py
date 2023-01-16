

#피보나치는 어차피 1값을 계속 재귀로 찾아야하기 때문에 그대로 가도 됨

def fib(n):

    if n==1 or n==2:
        return 1                           #코드1
    else:
        
        return (fib(n-1) + fib(n-2))



#DP는 주어진 경우의 개수를 찾기위해 dp_num 추가
def fibonacci(n):
    
    f= [x for x in range(n)]
    f[1],f[2] = 1,1
    dp_num=0
    for i in range(2,n):
        dp_num+=1
        f[i] = f[i-1] + f[i-2]              #코드2
    return dp_num


n= int(input())

print(fib(n),fibonacci(n))
