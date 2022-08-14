a= int(input())

c=list()

for i in range(a):
    b=input()

    s= list(b)
    count = 0
    c=1
    for i in s:
        if i=="O":
            count+=c
            c+=1
        else:
            c=1

    print(count)
        

        
    


