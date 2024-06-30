A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# a) Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó.
int_list = [int(item) for item in A]

Value = A[3]**2

A[3] = Value

print("ket qua: ", Value)
print(A)

# b) Xóa phần tử thứ 3 của list A bằng ít nhất hai cách khác nhau (gợi ý: sử dụng hàm pop hoặc hàm delete).
A.pop(3)
print(A)
del A[2]
print(A)

# c) Thêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần tử cuối cùng của list A
binh_phuong = A[-1]**2

A.append(binh_phuong)
print(A)

#d) Tính số phần tử trong list.

count = len(A)
print(count)

# e) Tính tổng các phần tử trong list.
total = sum(A)
print(total)

#f) Tính tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list.
tong = A[1] + A[2] + A[3] + A[5] 
print(tong)

phan_tu = [A[1], A[2], A[3], A[5]]
ss = sum(phan_tu)
print(ss)

# g) Tạo ra một list mới có thứ tự các phần tử đảo ngược với một list đã cho (bằng ít nhất hai cách khác nhau).
A.reverse()
print(A)

dao_nguoc = list(reversed(A))
print(dao_nguoc)

# h) Tách list ban đầu thành hai list, một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.
so_chan = []
so_le = []

for i in A:
    if i % 2 == 0:
        so_chan.append(i)
    else:
        so_le.append(i)
print(so_le)
print(so_chan)

#i) Tạo một list B gồm các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái qua phải.
#C1
B = sorted(A, reverse=True)
print(B)

#C2
A.sort(reverse=True)
b = A 
print(b)

# j) So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp,
# số phần tử của một list không thay đổi.
print(len(A))
print(len(B))

# k) Ghép hai list A và list B lại với nhau thành list C.