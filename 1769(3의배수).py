def Three_Multiple(num):
    global count
    global result
    a=[]
    
    if int(num)<10 :
        result=int(num)
        if result ==3 or result ==6 or result ==9:
            
            print(count)
            print("YES")
        else:
            print(count)
            print("NO")
        

    else:
        count+=1
        for i in num:
            a.append(int(i))   
        result=sum(a)

        return Three_Multiple(str(result))


count=0
X = input()
Three_Multiple(X)


        
        
    
        



