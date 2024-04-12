chuoi_vao = input("Nhập một chuỗi ký tự: ")
chuoi_so = ''.join([char for char in chuoi_vao if char.isdigit()])
if chuoi_so.isdigit():
    so = int(chuoi_so)
    la_so_nguyen_to = True
    if so <= 1:
        la_so_nguyen_to = False
    else:
        for i in range(2, int(so**0.5) + 1):
            if so % i == 0:
                la_so_nguyen_to = False
                break
    if la_so_nguyen_to:
        print(f"{so} là một số nguyên tố.")
    else:
        print(f"{so} không phải là số nguyên tố.")
else:
    print("Chuỗi ký tự không chứa số nguyên.")
