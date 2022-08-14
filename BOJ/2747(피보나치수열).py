
"""

재귀를 사용했으나 시간복잡도에 의해 시간초과가 일어남

def fib(n):

    if n<2:
        return n
    else:
        return fib(n-1)+fib(n-2)
    



n=int(input())


print(fib(n))
"""

#for문으로 대체

n=int(input())
a=0
b=1

for i in range(1,n):
    temp=b
    b=a+b
    a=temp
    
    
    


print(b)
