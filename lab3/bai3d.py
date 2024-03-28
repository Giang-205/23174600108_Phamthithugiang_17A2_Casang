#In ra số hoàn hảo bé hơn 500
for n in range(1,500):
    sum=0
    for i in range(1,n):
        if n % i ==0:
            sum+=i
    if sum == n :
        print(n)
    
