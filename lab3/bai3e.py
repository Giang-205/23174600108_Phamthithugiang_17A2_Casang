#In ra tổng của các số ngũ giác trong đoạn từ 1 đến 200
for i in range(1,201):
    P = i * (3*i-1) //2
    if P <= 201:
        print(P, end = ",")