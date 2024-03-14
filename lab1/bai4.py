dodai = int(input("Nhập độ dài cạnh đáy:"))
chieucao = int(input("Nhập chiều cao:"))
import math
#Diện tích xung quanh hình chóp tứ giác đều
L = 1/2 * dodai * 4 * chieucao
#Diện tích toàn phần của hình chóp tứ giác đều 
A = L + (dodai**2 *math.sqrt(3))/4
#Thể tích của hình chóp tứ giác đều
V = 1/3 * (dodai**2 *math.sqrt(3))/4 * chieucao
#In ra kêt quả
print("---------------------------------------")
print(f"""Độ dài cạnh đáy là: {dodai} chiều cao honhf chóp là : {chieucao}""")
print("Diện tích xung quanh của hình chóp tứ giác đều là: ", round(L,2))
print("Diện tích toàn phần của hình chóp tứ giác đều là:",round(A,2))
print("Thể tích của hình chóp tứ giác đều là:",round(V,2))