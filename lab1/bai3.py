sotienbandau = 10000
laisuatnam = 0.6
#Tính số tiền lãi sau 5 năm
amount_after_5_years = sotienbandau * (1+laisuatnam)**5

#Tính số tiền lãi sau 10 năm
amount_after_10_years = sotienbandau * (1+laisuatnam)**10

#Tính toán tỉ lệ tăng trưởng của số tiền sau 10 năm so với số tiền bạn đã có sau 5 năm
growth_1 = (amount_after_5_years - sotienbandau)/sotienbandau
growth_2 = (amount_after_10_years - sotienbandau)/sotienbandau
growth_rate = growth_2 - growth_1

#In kết quả
print("Số tiền sau 5 năm là :",round(amount_after_5_years,2))
print("Số tiền sau 10 năm là:",round(amount_after_10_years,2))
print("Tỷ lệ tăng trưởng sau 10 năm so với 5 năm là:",round(growth_rate,2),"%")