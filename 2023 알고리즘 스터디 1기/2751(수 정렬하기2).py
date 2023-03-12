

import sys

N = int(input())

num_list = []
for i in range(N):
    
    a= int(int(sys.stdin.readline()))
    num_list.append(a)

'''
b = len(num_list)
for i in range(b):
    min_list = i
    for j in range(i+1,b):
        if num_list[j] <num_list[min_list]:
            min_list = j
    num_list[min_list], num_list[i] = num_list[i] ,num_list[min_list] 

for i in num_list:
    print(i)
'''  


num_list.sort()

for i in num_list:
    print(i)
