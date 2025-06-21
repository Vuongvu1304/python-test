#Bài 6: Giải phương trình bậc nhất: ax + b = 0
#dùng map,float

a,b = map(float, input("Nhập a b: ").split())
if a == 0 and b == 0:
    print("Vo so nghiem")
elif a == 0:
    print("Vo nghiem")
else:
    x = -b / a
    print(f"{x:.2f}")
