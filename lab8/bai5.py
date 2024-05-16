def tong_uoc_so_chinh(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

def kiem_tra_amicable(a, b):
    tong_a = tong_uoc_so_chinh(a)
    tong_b = tong_uoc_so_chinh(b)
    return tong_a == b and tong_b == a
so1 = int(input("Nhập số 1 :"))
so2 = int(input("Nhập số 2 :"))
if kiem_tra_amicable(so1, so2):
    print(so1, "và", so2, "là một cặp số amicable.")
else:
    print(so1, "và", so2, "không phải là một cặp số amicable.")
