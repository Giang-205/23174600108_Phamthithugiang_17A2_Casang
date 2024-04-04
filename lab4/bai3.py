# Viết chương trình nhập vào một số nguyên và in ra chữ số của số  nguyền đó
n = int(input("Nhập số nguyên từ bàn phím: "))
count = 0
while n>0:
    count+=1
    n //=10
print("Số chữ số của số nguyên:",count)
