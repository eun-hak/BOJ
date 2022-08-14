#2022.01.14 10828(스택)문제


def push(x):                    #정수를 스택에 넣는 연산
    stack.append(x)

def pop():                      #스택 가장위에 정수를 빼고 그 수를 출력
    if len(stack) ==0:
        return-1

    if not stack:
        return -1
    else:
        return stack.pop()
    
def size():                     #스택에 들어있는 정수 개수 출력
    return len(stack)

def empty():                    #스택이 비어있으면1 아니면 0 출력
    if len(stack)==0:
        return 1
    else:
        return 0

def top():                      #가장 위의 정수를 출력, 없는경우 -1 출력
    return stack[-1] if stack else -1



import sys
N = int(input())   #이 개수만큼 반복
stack = []


#sys.stdin.readlin() => 반복문으로 여러줄 입력받을때는 input() 대신 사용
#                       여러줄에 input() 사용시 시간초과 문제
#rstrip()            => 오른쪽 공백 삭제 
#split()             => 문자열 분리
for _ in range(N):
    input_split = sys.stdin.readline().rstrip().split()
    cmd = input_split[0]
    if cmd == "push":
        push(input_split[1])
    elif cmd == "pop":
        print(pop())
    elif cmd == "size":
        print(size())
    elif cmd == "empty":
        print(empty())
    elif cmd == "top":
        print(top())



        
