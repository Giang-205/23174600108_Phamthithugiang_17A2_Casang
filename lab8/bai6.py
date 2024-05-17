#chương trình có thể lọc các số lẻ trong một danh sách bằng cách sử dụng hàm filter
def loc_so_le(numbers):
    return list(filter(lambda x: x % 2 != 0, numbers))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
so_le = loc_so_le(numbers)
print("Các số lẻ trong danh sách:", so_le)
#chương trình có thể lọc các số chẵn trong một danh sách bằng cách sử dụng hàm filter
def loc_so_chan(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
so_chan = loc_so_chan(numbers)
print("Các số chẵn trong danh sách:", so_chan)
#chương trình sử dụng hàm map() để tạo ra một danh sách trong đó các phần tử là lập phương của các phần tử trong danh sách ban đầu
def lap_phuong(numbers):
    return list(map(lambda x: x ** 3, numbers))
numbers = [1, 2, 3, 4, 5]
l_phuong = lap_phuong(numbers)
print("Danh sách các lập phương:", l_phuong)
#chương trình sử dụng hàm map() và filter() để tạo ra một danh sách trong đó các phần tử là lập phương của các số chẵn trong một danh sách đã cho.
def lap_phuong_so_chan(numbers):
    so_chan = filter(lambda x: x % 2 == 0, numbers)
    return list(map(lambda x: x ** 3, so_chan))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l_phuong_so_chan = lap_phuong_so_chan(numbers)
print("Danh sách các lập phương của số chẵn:", l_phuong_so_chan)
#chương trình sử dụng hàm map() và filter() để tạo ra một danh sách trong đó các phần tử là bình phương của các số lẻ trong một danh sách đã cho
def binh_phuong_so_le(numbers):
    so_le = filter(lambda x: x % 2 != 0, numbers)
    return list(map(lambda x: x ** 2, so_le))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b_phuong_so_le = binh_phuong_so_le(numbers)
print("Danh sách các bình phương của số lẻ:", b_phuong_so_le)


