#Bài 5: Kiểm tra tam giác và phân loại

#nhập 3 cạnh dùng map()
a,b,c = map(int,input("Nhập 3 cạnh: ").split())
#Kiểm tra điều kiện
if a + b <= c or a+c <= b or c+b <= a:
    print("Khong hop le")
elif a == b == c:
    print("Tam giac deu")
elif a == b or b == c or a == c:
    print("Tam giac can")
elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print("Tam giac vuong")
else:
    print("Tam giac thuong")
