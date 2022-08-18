S =int(input())


Answer = 0
a=1
count = 0
while True:
    Answer+=a
    count+=1
    if Answer>S:
        count-=1
        break  
    a+=1



print(count)

    
