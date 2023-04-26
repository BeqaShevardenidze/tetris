import os
def Cls():
    os.system("cls")
Cls()


def f_triangule():
    triangle1 = "  []  "
    triangle2 = "[][][]"
    triangle = (f"{triangle1}\n{triangle2}")
    return triangle

def f_triangule_right():
    triangule1 = "[]"
    triangule2 = "[][]"
    triangule3 = "[]"
    triangule = (f"{triangule1}\n{triangule2}\n{triangule3}")
    return triangule

def f_triangule_backwards():
    triangule1 = "[][][]"
    triangule2 = "  []  "
    triangule = (f"{triangule1}\n{triangule2}")
    return triangule

def f_triangule_left():
    triangule1 = "  []"
    triangule2 = "[][]"
    triangule3 = "  []"
    triangule = (f"{triangule1}\n{triangule2}\n{triangule3}")
    return triangule


if __name__ == "__main__":
    # print(f_triangule())
    # print(f_triangule_right())
    print(f_triangule_backwards())