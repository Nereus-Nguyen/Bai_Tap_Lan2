import matplotlib.pyplot as plt
import math


def khoang_cach (A, B):
    x1, y1 = A
    x2, y2 = B

    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    angle = math.radians(60)
    #xoay diem B 1 goc 60
    x3 =  (x2 - x1) * math.cos(angle) - (y2 - y1) * math.sin(angle)
    y3 =  (x2 - x1) * math.sin(angle) + (y2 - y1) * math.cos(angle)
    
    return x3 , y3

def creat_oxy(A, B, C):
    fig, ax = plt.subplots()

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    ax.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], 'go-')

    ax.grid(which = "both", color = "black", linewidth = 0.3)
 
    ax.text(A[0], A[1], 'A', fontsize = 12, ha = 'right')

    ax.set_xticks(range(0, 10, 1))
    ax.set_yticks(range(0, 10, 1))

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    plt.show()

A = (0, 0)
B = (2, 0)

x3, y3 = khoang_cach(A, B)

creat_oxy(A, B, [x3, y3])
