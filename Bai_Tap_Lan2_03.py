#day la comment by toan
def student_infomation (student_name, index_name, week_index, exercise_index):
    ten_file = f"{student_name}_{index_name}_Tuan{week_index}_Bai{exercise_index}.py"
    return ten_file
ten_file  = student_infomation("Nguyen_Thanh_Nhan", 22667121, 2, 3)
print(ten_file)
