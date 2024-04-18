n = input("Nhập số lượng phần tử trong mảng: ")
if n.isdigit() and int(n) > 0:
    n = int(n)
    mang = []
    for i in range(n):
        phan_tu = input(f"Nhập phần tử thứ {i + 1}: ")
        if phan_tu.isdigit() and int(phan_tu) > 0:
            mang.append(int(phan_tu))
        else:
            print("Phần tử phải là một số nguyên dương.")
            break
    else:
        so_nguyen_to = [num for num in mang if all(num % i != 0 for i in range(2, int(num**0.5) + 1)) and num > 1]
        so_hoan_hao = [num for num in mang if num == sum(i for i in range(1, num) if num % i == 0) and num > 0]
        
        print("Các số nguyên tố trong mảng:", so_nguyen_to)
        print("Các số hoàn hảo trong mảng:", so_hoan_hao)
else:
    print("Số lượng phần tử phải là một số nguyên dương.")
