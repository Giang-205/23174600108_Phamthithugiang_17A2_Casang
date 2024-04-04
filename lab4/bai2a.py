#Viết chương trình in ra các số nguyên tố nhỏ hơn 100
n = 2
while n <100:
    check = True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            check = False
            break
    if check:
        print(n,end=' , ')
    n+=1
        