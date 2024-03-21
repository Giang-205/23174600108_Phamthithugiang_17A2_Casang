print("Các thể loại phim đang có: Hành động , Kinh dị , Tình cảm , Hài hước , Hoạt hình")
loai_phim = input("Nhập thể loại phim bạn muốn xem : ")
thoi_gian = input("Chọn thời gian xem phim (sáng, trưa, chiều, tối): ")
if loai_phim == "Hành động":
    if thoi_gian in ["sáng","trưa","chiều","tối"]:
        print(f"Phim Hành động sẽ được chiếu vào buổi {thoi_gian}")
    else:
        print("Không có suất chiếu")
if loai_phim == "Kinh dị":
    if thoi_gian =="tối":
        print("Phim Kinh dị sẽ được chiếu vào buổi tối")
    else:
        print("Không có suất chiếu")
if loai_phim == "Tình cảm":
    if thoi_gian =="tối":
        print("Phim Hành động sẽ được chiếu vào buổi tối")
    else:
        print("Không có suất chiếu")
if loai_phim == "Hài hước":
    if thoi_gian in ["sáng","trưa","chiều","tối"]:
        print(f"Phim Hài hước sẽ được chiếu vào buổi {thoi_gian}.")
    else:
        print("Không có suất chiếu")
if loai_phim == "Hoạt hình":
    if thoi_gian in ["sáng","trưa"]:
        print(f"Phim Hoạt hình sẽ được chiếu vào buổi {thoi_gian}.")
    else:
        print("Không có suất chiếu")
else:
    print("thể loại phim không hợp lệ!")




      


