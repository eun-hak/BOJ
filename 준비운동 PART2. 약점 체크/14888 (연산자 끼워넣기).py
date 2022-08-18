import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
Plus,Minus,Multiple,Divide = map(int,input().split())

#1e9는 10**9
maximum = -1e9
minimum = 1e9



def recursion(idx,total_num, plus, minus, multiply, divide):
    global maximum
    global minimum
    if idx == N:
        maximum = max(total_num, maximum)
        minimum = min(total_num , minimum)


        return

    #내가 헷갈린 부분
    #### 파이썬에서는  2, 8 ,10진수와 관계없이 0이면 거짓 / 0이 아니면 참이다####
    if plus:
        recursion(idx + 1, total_num + A[idx], plus - 1, minus, multiply, divide)
    if minus:
        recursion(idx + 1, total_num - A[idx], plus, minus - 1, multiply, divide)
    if multiply:
        recursion(idx + 1, total_num * A[idx], plus, minus, multiply - 1, divide)
    if divide:
        recursion(idx + 1, int(total_num / A[idx]), plus, minus, multiply, divide - 1)




recursion(1,A[0],Plus,Minus,Multiple,Divide)

print(maximum)
print(minimum)
