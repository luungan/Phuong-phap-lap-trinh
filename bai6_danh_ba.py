# Bài 6: Quản lý danh bạ

def add_contact(danh_ba):
    ten = input("Nhập tên: ")
    sdt = input("Nhập số điện thoại: ")
    contact = ten + " - " + sdt
    danh_ba.append(contact)
    print("Đã thêm liên hệ thành công!")


def show_contacts(danh_ba):
    if len(danh_ba) == 0:
        print("Chưa có liên hệ nào")
    else:
        print("Danh sách liên hệ:")
        for i, contact in enumerate(danh_ba, start=1):
            print(f"{i}. {contact}")


def search_contact(danh_ba):
    ten_can_tim = input("Nhập tên cần tìm: ")
    found = False

    for contact in danh_ba:
        if ten_can_tim.lower() in contact.lower():
            print("Tìm thấy:", contact)
            found = True

    if not found:
        print("Không tìm thấy")


def hien_thi_menu():
    print("\n=== HỆ THỐNG QUẢN LÝ DANH BẠ ===")
    print("1. Thêm liên hệ mới")
    print("2. Hiển thị tất cả danh bạ")
    print("3. Tìm kiếm liên hệ")
    print("4. Thoát")


def main():
    my_contacts = []

    while True:
        hien_thi_menu()
        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            add_contact(my_contacts)

        elif choice == "2":
            show_contacts(my_contacts)

        elif choice == "3":
            search_contact(my_contacts)

        elif choice == "4":
            print("Thoát chương trình")
            break

        else:
            print("Lựa chọn không hợp lệ!")


# Chạy chương trình
main()