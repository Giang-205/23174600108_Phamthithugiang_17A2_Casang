#số chính phương
for i in range(1,1001):
    n=int(i**0.5)
    if n * n == i:
        print(i ,",",end='')
