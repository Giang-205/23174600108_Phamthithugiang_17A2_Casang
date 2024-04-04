#Viết chương trình nhập vào các số nguyên dương từ bàn phím cho đến khi tổng các số đã nhập vượt quá 1000
#Đếm số lượng số nguyên đã nhập
count = 0
total = 0
while total <= 1000:
    n = int(input("Nhập số nguyên dương:"))
    if n>0:
        total += n
        count += 1
print("Số lượng số nguyên đã nhập:", count)