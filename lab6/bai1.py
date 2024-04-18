n = input("Nhập số lượng phần tử trong mảng: ")
if n.isdigit() and int(n) > 0:
    n = int(n)
    mang_phan_tu = []
    for i in range(n):
        phan_tu = input("Nhập phần tử thứ {}: ".format(i + 1))
        if phan_tu.isdigit() and int(phan_tu) > 0:
            mang_phan_tu.append(int(phan_tu))
        else:
            print("Phần tử phải là số nguyên dương.")
            break
    else:
        tong_chan = sum(num for num in mang_phan_tu if num % 2 == 0)
        tong_le = sum(num for num in mang_phan_tu if num % 2 != 0)
        print("Tổng các số chẵn trong mảng:", tong_chan)
        print("Tổng các số lẻ trong mảng:", tong_le)
else:
    print("Số lượng phần tử phải là số nguyên dương.")
