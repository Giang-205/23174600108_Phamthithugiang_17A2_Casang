#Viết chương trình nhập vào các số nguyên dương từ bàn phím cho đến khi tổng các số đã nhập vượt quá 1000
#Các số chẵn đã nhập
a = []
total = 0
while total <= 1000:
    n = int(input("Nhập số nguyên dương:"))
    if n>0:
        total += n
        if n % 2 == 0:
            a.append(n)
print("Các số lẻ đã nhập:", a)