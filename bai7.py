#Bài 7: Giải phương trình bậc hai: ax^2 + bx + c = 0
#dùng map,float   NOTE:            dental = b^2 - 4 a.c
#giải theo 2 trường hơp a= 0 và a khác 0
#Dùng int(x) để kiểm tra nếu là số nguyên (ví dụ 2.0 thì in ra 2)
#Dùng round(x, 2) để làm tròn nếu không phải số nguyên

a,b, c = map(float, input("Nhập a b c: ").split())

if a == 0:
    if b == 0:
        if c == 0:
            print("Vô số nghiệm")
        else:
            print("Vô nghiệm")
    else:
        x = -c / b
        if x == int(x):
            print(int(x))
        else:
            print(round(x, 2))
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Vô nghiệm")
    elif delta == 0:
        x = -b / (2*a)
        if x == int(x):
            print(int(x))
        else:
            print(round(x, 2))
    else:
        x1 = (-b + delta**0.5)/(2*a)
        x2 = (-b - delta**0.5)/(2*a)
        if x1 > x2:
            x1, x2 = x2, x1
            if x1 == int(x1):
                print(int(x1), end=' ')
            else:
                print(round(x1, 2), end=' ')

            if x2 == int(x2):
                print(int(x2))
            else:
                print(round(x2, 2))
