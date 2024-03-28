sum=0
for i in range(2000,4001):
    if (i % 7 == 0) and (i % 5 != 0):
        sum+=i
print("Tổng:",sum)

