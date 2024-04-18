n = input("Nhập số lượng số Fibonacci muốn tạo: ")
if n.isdigit() and int(n) >= 0:
    n = int(n)
    fibonacci = [0, 1] + [0]*(n - 2 if n >= 2 else 0)
    for i in range(2, n):
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
    print("Danh sách Fibonacci:", fibonacci)
else:
    print("Vui lòng nhập một số nguyên dương.")
