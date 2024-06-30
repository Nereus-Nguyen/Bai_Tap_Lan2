TK = int(input("Diem thuong ki: "))
GK = int(input("Diem giua ki: "))
CK = int(input("Diem cuoi ki: "))

def trung_binh (TK, GK ,CK):
    average = int(TK * 0.2 + GK * 0.3 + CK * 0.5)
    if average < 4 :
        print("F")
    elif average >= 4 & average <= 5.4 :
        print("D")
    elif average > 5.4 & average <= 6.9 :
        print("C")
    elif average > 6.9 & average <= 8.4:
        print("B")
    else:
        print("A")
    return 

trung_binh(TK, GK, CK)
