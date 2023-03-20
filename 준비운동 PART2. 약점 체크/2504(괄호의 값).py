array = list(input())

stack = []
answer = 0
tmp = 1

for i in range(len(array)):
    if array[i] == "(":
        stack.append(array[i])
        tmp*=2
        
    
    elif array[i]  =="[":
        stack.append(array[i])
        tmp*=3
        

        
    elif array[i]  ==")":
        if not stack or stack[-1] == "[":       #[)를 의미함
            answer = 0
            break
        if array[i-1] =="(":
          
            answer+=tmp
        stack.pop()
        tmp//=2

    else:
        if not stack or stack[-1] == "(":           #(]를 의미함
            answer = 0
            break
        if array[i-1] == "[":
           
            answer+=tmp
        stack.pop()
        tmp//=3

if stack:
    print(0)
else:
    print(answer)
#괄호가 연속되면 tmp로 계속 곱하게됨
#누적 계산임 [()[]] 이걸 예시로두면 [() 이걸 계산할 때 이미 곱하기가 되어있음
#하넙에 곱하는게 아니고 순차적으로 곱하는 방식

#[()[]]
