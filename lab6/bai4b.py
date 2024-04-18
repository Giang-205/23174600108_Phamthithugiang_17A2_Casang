so_nguyen_to = [num for num in range(2, 100) if all(num % i != 0 for i in range(2, int(num**0.5) + 1)) and num > 1]
print("Danh sách các số nguyên tố nhỏ hơn 100:", so_nguyen_to)
