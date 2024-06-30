#Viết một hàm tìm tất cả các nghiệm thực (phân biệt) của phương trình ax2+bx+c=0.
import math
a = float(input("Nhap gia tri a: "))
b = float(input("Nhap gia tri b: "))
c = float(input("Nhap gia tri c: "))

del_ta = (b**2) - (4*a*c)
if del_ta < 0:
    print("Phuong trinh vo nghiem")
    
elif del_ta == 0:
    x0 = -b / 2*a
    
else:
    x1 = (-b + math.sqrt(del_ta))/ (2*a)
    x2 = (-b - math.sqrt(del_ta))/ (2*a)
    print(f"nghiem thu 1: x1 = {x1}, nghiem thu 2: x2 = {x2}")