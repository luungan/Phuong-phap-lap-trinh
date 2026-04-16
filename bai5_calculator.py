# Hàm cộng
def cong(a, b):
    return a + b
# Hàm trừ
def tru(a, b):
    return a - b
# Hàm nhân
def nhan(a, b):
    return a * b
# Hàm chia
def chia(a, b):
    if b == 0:
        print("Lỗi chia cho 0")
        return None
    return a / b
# Hiển thị menu
def hien_thi_menu():
    print("\n===== MENU =====")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("5. Thoát")
# Chương trình chính
while True:
    hien_thi_menu()
    choice = input("Chọn chức năng (1-5): ")

    if choice == "5":
        print("Thoát chương trình")
        break

    if choice in ["1", "2", "3", "4"]:
        a = float(input("Nhập số a: "))
        b = float(input("Nhập số b: "))

        if choice == "1":
            print("Kết quả:", cong(a, b))
        elif choice == "2":
            print("Kết quả:", tru(a, b))
        elif choice == "3":
            print("Kết quả:", nhan(a, b))
        elif choice == "4":
            result = chia(a, b)
            if result is not None:
                print("Kết quả:", result)
    else:
        print("Lựa chọn không hợp lệ!")