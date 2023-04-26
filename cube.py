import os
def Cls():
    os.system("cls")
Cls()

def f_standart_cube():
    cube1 = "[][]"
    cube2 = "[][]"
    cube = (f"{cube1}\n{cube2}")
    return cube


if __name__ == "__main__":
    print(f_standart_cube())