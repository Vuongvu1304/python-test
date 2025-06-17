#Quy tắc năm nhuận:
#Một năm là năm nhuận nếu:
#Chia hết cho 4 và không chia hết cho 100 hoặc Chia hết cho 400
# Ví dụ:
#2024: chia hết cho 4 và không chia hết cho 100 →  năm nhuận
#1900: chia hết cho 100 nhưng không chia hết cho 400 →  không phải năm nhuận
#2000: chia hết cho 400 →  năm nhuận

#bài 4:Kiểm tra năm nhuận
year= int(input("Nhập năm: "))

if year <= 0:
    print("INVALID")
else:
    #kiểm tra năm nhuận
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("YES")
    else:
        print("NO")
