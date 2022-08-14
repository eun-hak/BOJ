n,k = map(int,input().split())

#이항계수 공식을 사용하여 함수를 만듬

def pac(n):

    if n <=1:
        return 1
    else:
        return n*pac(n-1)





print(int(pac(n)/(pac(k)*pac(n-k))))


