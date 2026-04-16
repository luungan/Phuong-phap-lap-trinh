import math

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

# Phần 1: kiểm tra 1 số
n = int(input("Nhập số: "))

if is_prime(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không phải số nguyên tố")

# Phần 2: in từ 1 đến 100
print("Các số nguyên tố từ 1 đến 100:")

for i in range(1, 101):
    if is_prime(i):
        print(i, end=" ")