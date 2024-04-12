chuoi = input("Nhập chuỗi văn bản: ")
tu_can_tim = input("Nhập từ cần tìm kiếm: ")
vi_tri = chuoi.find(tu_can_tim)
if vi_tri != -1:
    print(f"Từ '{tu_can_tim}' nằm ở ví trí {vi_tri} trong chuỗi.")
else:
    print(f"Từ '{tu_can_tim}' không xuất hiện trong chuỗi.")

words = chuoi.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1 
tu_tim_nhieu_nhat = max(word_count, key=word_count.get)
max_count = word_count [tu_tim_nhieu_nhat]
print(f"Từ xuất hiện nhiều nhất trong chuỗi là '{tu_tim_nhieu_nhat}' với {max_count} là xuất hiện")

 