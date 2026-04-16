# Hàm tìm số lớn nhất
def find_max(lst):
    max_value = lst[0]  # giả sử phần tử đầu là lớn nhất
    for x in lst:
        if x > max_value:
            max_value = x
    return max_value

# Hàm tìm số nhỏ nhất
def find_min(lst):
    min_value = lst[0]  # giả sử phần tử đầu là nhỏ nhất
    for x in lst:
        if x < min_value:
            min_value = x
    return min_value
diem_so = [6.5, 8.0, 4.5, 9.5, 7.0]

print("Danh sách:", diem_so)
print("Số lớn nhất:", find_max(diem_so))
print("Số nhỏ nhất:", find_min(diem_so))