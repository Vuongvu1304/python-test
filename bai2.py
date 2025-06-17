#Bài 2:Xếp loại học lực
#Bước 1: Nhập 3 đầu điểm Toán,Văn,Anh
toan = int(input("Nhập điểm môn Toán: "))
van = int(input("Nhập điểm môn Văn: "))
anh = int(input("nhập điểm môn Anh: "))

#Bước 2:xử lý dữ liệu đầu vào

if toan < 0 or van < 0 or anh < 0:
    print("Điểm không thể nhỏ hơn 0")
elif toan > 10 or van > 10  or anh > 10:
    print("Điểm không thể lớn hơn 10")
else:
    #tính điểm trung bình
    tb =(toan + van + anh)/3
    #làm tròn 2 chữ số sau dấu phẩy
    tb_round = round(tb, 2)

    #Bước 3:Xếp loại học lực:
    if tb >= 8:
        loai = "Gioi"
    elif tb >=6 :
        loai = "Kha"
    elif tb >= 5 :
        loai = "Trung binh"
    else:
        loai = "Yeu"
    #Bước 4:in ra kết quả:
    if tb_round == int(tb_round):
        print(int(tb_round), loai)
    else:
        print(tb_round, loai)
