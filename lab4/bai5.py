#Viết chương trình thực hiện các phép tính số học trên 2 số nhập từ người dùng và cho phép người dùng tiếp tục nếu muốn
a, b = map(int, input("Nhập vào hai số a và b: ").split())
print(
"""
Chương trình hiển thị menu chọn phép tính số học:
1. Phép cộng 2 số
2. Phép trừ 2 số
3. Phép nhân 2 số
4. Phép chia 2 số
5. Phép lũy thừa 2 số
6. Phép tính căn bậc hai của 2 số
"""
)
import math
lua_chon = int(input("Nhập vào lựa chọn: "))
while True:
    if lua_chon == 1:
        print(f"Tổng 2 số là: {a} + {b} = {a + b}")
        break
    elif lua_chon == 2:
        print(f"Hiệu 2 số là: {a} - {b} = {a - b}")
        break
    elif lua_chon == 3:
        print(f"Tích 2 số là: {a} x {b} = {a * b}")
        break
    elif lua_chon == 4:
        print(f"Thương 2 số là: {a} : {b} = {a / b}")
        break
    elif lua_chon == 5:
        print(f"Lũy thừa 2 số là: {a} ** {b} = {a**b}")
        break
    elif lua_chon == 6:
        print(f"Căn bậc hai của 2 số là: {a},{b} = {math.sqrt(a)} , {math.sqrt(b)}" )
        break
    n = input("bạn có muốn tiếp tục không? (c/k):")
    if n == 'k':
        break