import math
def hoan_vi(n, r):
    return math.factorial(n) // math.factorial(n - r)
def to_hop(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
n = int(input("Nhập giá trị của n: "))
r = int(input("Nhập giá trị của r: "))
ket_qua_hoan_vi = hoan_vi(n, r)
ket_qua_to_hop = to_hop(n, r)
print("Số hoán vị của", n, "phần tử lấy", r, "phần tử mỗi lần là:", ket_qua_hoan_vi)
print("Số tổ hợp của", n, "phần tử lấy", r, "phần tử mỗi lần là:", ket_qua_to_hop)
