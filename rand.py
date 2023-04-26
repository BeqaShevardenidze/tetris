from cube import f_standart_cube
from triangle import *
from line import *
from zigzag import *
from zigzag_mirror import *
from l_block import *
from l_block_mirror import *

def f_rand():
    import os
    import random
    def Cls():
        os.system("cls")
    # Cls()

    Cube = f_standart_cube()

    triangule = f_triangule()
    triangule_right = f_triangule_right()
    triangule_backwards = f_triangule_backwards()
    triangule_left = f_triangule_left()

    line = f_line()
    line_height = f_line_height()

    zigzag_right = f_zigzag_right()
    zigzag_height = f_zigzag_height()

    zigzag_mirror = f_zigzag_mirror()
    zigzag_mirror_height = f_zigzag_mirror_height()

    l_block = f_l_block()
    l_block_height = f_l_block_height()

    l_block_mirror = f_l_block_mirror()
    l_block_mirror_height = f_l_block_mirror_height()

    # ========================================


    my_list = (l_block_mirror,
    l_block_mirror_height,Cube,triangule,triangule_right,triangule_backwards,triangule_left,line,line_height,zigzag_right,zigzag_height,zigzag_mirror,zigzag_mirror_height,l_block,l_block_height,)

    size = len(my_list)
    rand_num = random.randint(0, size-1)
    return my_list[rand_num]


if __name__ == "__main__":
    print(f_rand())


# print(Cube, "\n")

# print(triangule, "\n")
# print(triangule_right, "\n")
# print(triangule_backwards,"\n")
# print(triangule_left,"\n")

# print(line,"\n")
# print(line_height,"\n")

# print(zigzag_right,"\n")
# print(zigzag_height,"\n")

# print(zigzag_mirror,"\n")
# print(zigzag_mirror_height,"\n")

# print(l_block,"\n")
# print(l_block_height,"\n")

# print(l_block_mirror,"\n")
# print(l_block_mirror_height,"\n")

