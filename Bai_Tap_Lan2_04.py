#(a) Kiểm tra xem các từ khóa Python, contains, experience, difficult có tồn tại trong đoạn văn trên hay không?

text = """Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."""

# keyword = ['Python', 'contain','experience','difficult']

# for keyword in keyword:
#     if keyword in text:
#         print(f"the keyword '{keyword}' is persent in the text" )
#     else:
#         print(f"the keyword '{keyword}'NOT persent on the text")

# for keyword in keyword:
#     if keyword in text:
#         sum = keyword + 1
#         break
#     else:
#         print("Not keyword")
# keyword = 'Python'
# count = text.count(keyword)
# print(f"'{keyword}' appears {count} times in the text")


# def dem_tu_bang_split(van_ban):
#   """
#   Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). 
#   Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. 
#   Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.
#   """
#   # Chia nhỏ văn bản thành các từ
#   danh_sach_tu = van_ban.split()

#   # Đếm số lượng từ
#   so_luong_tu = 0
#   for i in danh_sach_tu:
#     so_luong_tu += 1
#   return so_luong_tu

# van_ban = "Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."
# so_luong_tu = dem_tu_bang_split(van_ban)
# print(f"Số lượng từ trong văn bản: {so_luong_tu}")


chuoi_moi = text.title()
print(f"Chuoi sau khi chuyen doi: {chuoi_moi}")