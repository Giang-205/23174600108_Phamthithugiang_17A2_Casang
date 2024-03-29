#số nguyên tố
for n in range(100,1001):
    check =True
    for j in range(2,n):
       
        if n%j==0:
            check=False
        
    if check==True :
        print(n,end=",")