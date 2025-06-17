# Bài 4: Kiểm tra ngày hợp lệ

# Nhập ngày, tháng, năm
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

# Kiểm tra năm hợp lệ
if year < 1 or month < 1 or month > 12 or day < 1:
    print("NO")
else:
    # Xác định số ngày tối đa trong tháng
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    elif month == 2:
        # Xử lý năm nhuận
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            max_day = 29
        else:
            max_day = 28
    else:
        max_day = 0  # Trường hợp không tồn tại

    # So sánh ngày nhập với max_day
    if day <= max_day:
        print("YES")
    else:
        print("NO")
