# Bài 1: Tính tiền taxi
# Nhập số km từ bàn phím
km = float(input("Nhập số km đã đi: "))
# Tính tiền
if km <= 1:
    tien = 15000
elif km <= 20:
    tien = 15000 + (km - 1) * 12000
else:
    tien = 15000 + 19 * 12000 + (km - 20) * 10000
# In kết quả
print("Số tiền phải trả là:", format(tien, ",.0f"), "VNĐ")