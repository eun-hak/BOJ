#input함수로 입력 (input함수는 출력이 문자이므로 int로 묶어줌)

N= int(input())

#입력받는 정수 개수의 제한이 없게끔 list로 묶어줌
#그 후 공백 기준으로 나누기 위해 split()사용
#똑같이 input은 출력이 문자이므로 map함수로 int로 묶어줌

nums = list(map(int,input().split()))



print(min(nums),max(nums))
 

