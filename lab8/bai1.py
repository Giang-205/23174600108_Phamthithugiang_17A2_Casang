def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def so_nguyen_to_sinh_doi():
    so_sinh_doi = []
    for num in range(3, 1000, 2):
        if la_so_nguyen_to(num) and la_so_nguyen_to(num + 2):
            so_sinh_doi.append((num, num + 2))
    return so_sinh_doi

cac_cap_so_sinh_doi = so_nguyen_to_sinh_doi()
for cap_so in cac_cap_so_sinh_doi:
    print(cap_so)
