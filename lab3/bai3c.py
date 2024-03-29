a, b = 0, 1
for i in range(11):
    a, b = b , a + b
    print(a, end=', ')