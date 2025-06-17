# Bài 9: Ký tự kế tiếp
c = input("Nhập ký tự: ")

if len(c) != 1:
    print("Vui lòng nhập một ký tự duy nhất!")
else:
    next_char = chr(ord(c) + 1)
    print("Ký tự kế tiếp là:", next_char)
