#Viết chương trình nhập một số từ bàn phím và in ra màn hình bằng chữ tiếng anh
n = int(input("Nhập số từ bàn phím: "))
count = 1
a = n 
while True: 
    a = a//10 
    if a == 0:
        break
    count += 1 

for i in range(count,0,-1):
    phan_nguyen = n//(10**(i-1))
    if phan_nguyen == 0:
        print("zezo", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 1:
        print("one", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 2:
        print("two", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 3:
        print("three", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 4:
        print("four", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 5:
        print("five", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 6:
        print("six", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 7:
        print("seven", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 8:
        print("eight", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 9:
        print("nine", end = " ")
        n = n % (10**(i-1))
        print("số được đọc là:")