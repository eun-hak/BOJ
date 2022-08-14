c=list()



S=input()


for i in S:
    c.append(i)


for j in range(97,123):
    if c.count(chr(j))>=1:
        print(c.index(chr(j)), end=" ")
        
    else:
        print(-1,end=" ")
        
    
