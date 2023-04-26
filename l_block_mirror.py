import os
def Cls():
    os.system("cls")
Cls()

def f_l_block_mirror():
    block1 = "    []"
    block2 = "[][][]"
    block = (f"{block1}\n{block2}")
    return block

def f_l_block_mirror_height():
    block1 = "[][]"
    block2 = "  []"
    block3 = "  []"
    block = (f"{block1}\n{block2}\n{block3}")
    return block




if __name__ == "__main__":
    print(f_l_block_mirror())