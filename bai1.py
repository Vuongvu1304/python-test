#Bai 1:Tính giá vé tham quan
các bước làm:
#Bước 1:Nhập tuổi từ người dùng
age = int(input("Nhập số tuổi: "))

#Bước 2:gán giá trị gốc
price = 100000

#Bước 3:Xử lý theo từng trường hợp
if age < 0 :
    print("INVALID")
elif age < 6 :
    print(0)   #Miễn phí
elif age <= 18 :
    print(price * 0.5)     #giảm 50% giá
elif age >= 60:
    print(price & 0.3)      #giảm 30%
else:
    print(price) #ko giảm,giá ban đầu
