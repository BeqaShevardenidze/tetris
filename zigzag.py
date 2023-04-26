import os
def Cls():
    os.system("cls")
Cls()

def f_zigzag_right():
    zigzag1 = "[][]  "
    zigzag2 = "  [][]"
    zigzag = (f"{zigzag1}\n{zigzag2}")
    return zigzag

def f_zigzag_height():
    zigzag1 = "  []"
    zigzag2 = "[][]"
    zigzag3 = "[]  "
    zigzag = (f"{zigzag1}\n{zigzag2}\n{zigzag3}")
    return zigzag


if __name__ == "__main__":
    # print(f_zigzag_right())
    print(f_zigzag_height())