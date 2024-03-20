# Nhập vào số nguyên có 3 chữ số,in ra cách đọc theo tiếng anh
n = int(input("Nhập vào số nguyên n: "))
if 100 <= n <= 999:
    chu_so_hang_tram = n // 100
    chu_so_hang_chuc = (n//10) % 10
    chu_so_hang_don_vi = n % 10
    # Đọc chữ số hàng trăm
    if chu_so_hang_tram == 1:
        doc_hang_tram = "One hundred"
    elif chu_so_hang_tram == 2:
        doc_hang_tram = 'Two hundred'
    elif chu_so_hang_tram == 3:
        doc_hang_tram = 'Three hundred'
    elif chu_so_hang_tram == 4:
        doc_hang_tram = 'Four hundred'
    elif chu_so_hang_tram == 5:
        doc_hang_tram = 'Five hundred'
    elif chu_so_hang_tram == 6:
        doc_hang_tram = 'Six hundred'
    elif chu_so_hang_tram == 7:
        doc_hang_tram = 'Seven hundred'
    elif chu_so_hang_tram == 8:
        doc_hang_tram = 'Eight hundred'
    elif chu_so_hang_tram == 9:
        doc_hang_tram = 'Nine hundred'
    elif chu_so_hang_tram == 0:
        doc_hang_tram = ''
    # Đọc chữ số hàng chục và hàng đơn vị
        #Khi hàng trục là 1
    if chu_so_hang_chuc == 1:  
        if chu_so_hang_don_vi == 0:
            doc_hang_chuc = 'ten'
        elif chu_so_hang_don_vi == 1:
            doc_hang_chuc  = 'eleven'
        elif chu_so_hang_don_vi == 2:
            doc_hang_chuc = 'twelve'
        elif chu_so_hang_don_vi == 3:
            doc_hang_chuc = 'thirteen'
        elif chu_so_hang_don_vi == 4:
            doc_hang_chuc = 'fourteen'
        elif chu_so_hang_don_vi == 5:
            doc_hang_chuc = 'fifteen'
        elif chu_so_hang_don_vi == 6:
            doc_hang_chuc = 'sixteen'
        elif chu_so_hang_don_vi == 7:
            doc_hang_chuc = 'seventeen'
        elif chu_so_hang_don_vi == 8:
            doc_hang_chuc = 'eighteen'
        elif chu_so_hang_don_vi == 9:
            doc_hang_chuc = 'nineteen'
    #không cần đọc hàng đơn vị khi chữ số hàng chục từ 10 đến 19
        doc_hang_don_vi = ''
    else:
        if chu_so_hang_chuc == 2:
            doc_hang_chuc = 'twenty'
        elif chu_so_hang_chuc == 3:
            doc_hang_chuc = 'thirty'
        elif chu_so_hang_chuc == 4:
            doc_hang_chuc = 'forty'
        elif chu_so_hang_chuc == 5:
            doc_hang_chuc = 'fifty'
        elif chu_so_hang_chuc == 6:
            doc_hang_chuc = 'sixty'
        elif chu_so_hang_chuc == 7:
            doc_hang_chuc = 'seventy'
        elif chu_so_hang_chuc == 8:
            doc_hang_chuc = 'eighty'
        elif chu_so_hang_chuc == 9:
            doc_hang_chuc = 'ninety'
        elif chu_so_hang_chuc == 0:
            doc_hang_chuc = ''
            #Đọc hàng đơn vị khi không phải hàng chục từ 10 đến 19
    if chu_so_hang_don_vi != 0 and chu_so_hang_chuc!=1:  
        if chu_so_hang_don_vi == 1:
                doc_hang_don_vi = "one"
        elif chu_so_hang_don_vi == 2 :
                doc_hang_don_vi = 'two'
        elif chu_so_hang_don_vi == 3:
                doc_hang_don_vi = 'three'
        elif chu_so_hang_don_vi == 4:
                doc_hang_don_vi = 'four'
        elif chu_so_hang_don_vi == 5:
                doc_hang_don_vi = 'five'
        elif chu_so_hang_don_vi == 6:
                doc_hang_don_vi = 'six'
        elif chu_so_hang_don_vi == 7:
                doc_hang_don_vi = 'seven'
        elif chu_so_hang_don_vi == 8:
                doc_hang_don_vi = 'eight'
        elif chu_so_hang_don_vi == 9:
                doc_hang_don_vi = 'nine'
        else:
            doc_hang_don_vi = ''
    print("Số", n, "đọc là:", doc_hang_tram, doc_hang_chuc, doc_hang_don_vi)
else:
    print("không hợp lệ, thử lại!")