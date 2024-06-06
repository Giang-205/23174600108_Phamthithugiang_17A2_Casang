import random
import csv
#1. Tạo một list để lưu trữ kết quả của mỗi lần tung xúc xắc
ket_qua = []
#2. Tạo một set để lưu trữ các tổng đã xuất hiện
tong_set = set()
#3. Tạo một dictionary để lưu trữ thông tin về xác suất xuất hiện của mỗi tổng
xac_suat_tong = {}
#4. Viết hàm
# Tung xúc xắc và trả về kết quả
def tung_xuc_xac():
    xuc_xac = []
    for i in range(3):
        xuc_xac.append(random.randint(1, 6))
    return xuc_xac
# Tính tổng của 3 xúc xắc
def tinh_tong(xuc_xac):
    return sum(xuc_xac)
# Kiểm tra xem người chơi đã đoán đúng tổng hay chưa
def kiem_tra_du_doan(dudoan, tong_dung):
    return dudoan == tong_dung
# Tính xác suất xuất hiện của mỗi tổng dựa trên các kết quả đã lưu trữ
def tinh_xac_suat(ket_qua):
    tong_so_lan_tung = len(ket_qua)
    xac_suat_tong.clear() 
    
    for ket_qua_tung_lan in ket_qua:
        tong_gia_tri = ket_qua_tung_lan['tong']
        if tong_gia_tri in xac_suat_tong:
            xac_suat_tong[tong_gia_tri] += 1
        else:
            xac_suat_tong[tong_gia_tri] = 1
    
    for tong_gia_tri, so_lan_xuat_hien in xac_suat_tong.items():
        xac_suat = so_lan_xuat_hien / tong_so_lan_tung
        xac_suat_tong[tong_gia_tri] = xac_suat

def luu_ket_qua_vao_csv(ten_file):
    with open(ten_file, 'w', newline='') as csvfile:
        cac_truong = ['Lần tung', 'Tổng', 'Kết quả', 'Xác suất']
        writer = csv.DictWriter(csvfile, fieldnames=cac_truong)
        
        writer.writeheader()
        for i, ket_qua in enumerate(ket_qua):
            writer.writerow({'Lần tung': i + 1, 'Tổng': ket_qua['tong'], 'Kết quả': ket_qua['ket_qua'], 'Xác suất': xac_suat_tong[ket_qua['tong']]})
# Sử dụng vòng lặp và câu điều kiện để kiểm soát quá trình trò chơi
def choi_game():
    ket_qua = [] 
    choi_tiep = True
    while choi_tiep:
        du_doan = int(input("Nhập dự đoán của bạn (từ 3 đến 18): "))
        if du_doan < 3 or du_doan > 18:
            print("Dự đoán không hợp lệ. Vui lòng nhập lại.")
            continue
        
        xuc_xac = tung_xuc_xac()
        tong_thuc = tinh_tong(xuc_xac)
        ket_qua_tung_lan = {'tong': tong_thuc, 'ket_qua': kiem_tra_du_doan(du_doan, tong_thuc)}
        ket_qua.append(ket_qua_tung_lan)  
        tong_set.add(tong_thuc)
        
        print("Kết quả của lần tung xúc xắc là:", xuc_xac)
        print("Tổng của ba xúc xắc là:", tong_thuc)
        print("Kết quả dự đoán của bạn là:", ket_qua_tung_lan['ket_qua'])
        
        tinh_xac_suat(ket_qua) 
        
        lua_chon = input("Bạn có muốn chơi lại không? (có/không): ")
        if lua_chon.lower() != 'có':
            choi_tiep = False
            ten_file = input("Nhập tên file để lưu kết quả: ")
            luu_ket_qua_vao_csv(ten_file, ket_qua) 
            print("Cảm ơn bạn đã chơi!")


# Chạy trò chơi
if __name__ == "__main__":
    choi_game()

