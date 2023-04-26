import os
def Cls():
    os.system("cls")
Cls()

from rand import f_rand
from board import f_board

# print(f_board())
# print(f_rand())

from time import sleep

my_list = ["."] * 10
my_list2 = ["."] * 10
my_list3 = ["."] * 10
my_list4 = ["."] * 10
my_list5 = ["."] * 10
# for i in range(len(my_list)):
#     print(my_list[i])

# print(my_list)

# my_list.pop(0)
# my_list.insert(0,"x")
# print(my_list)

# my_list.pop(0)
# my_list.insert(0,".")

# my_list.pop(1)
# my_list.insert(1,"x")
# print(my_list)



i = -1
for j in range(len(my_list)):
    print(my_list[j])
while True:
    sleep(1)
    Cls()
    i+=1
    my_list[i] = "x"
    for j in range(len(my_list)):
        print(my_list[j])

    if my_list[9] != "x":
        my_list[i] = "."
        
    if my_list[9] == "x":
        break


# # ////////////////my_list2
#     if my_list[9] == "x":
#         i = -1
#         while True:
#             sleep(1)
#             Cls()
#             i+=1
#             my_list2[i] = "x"
#             for j in range(len(my_list)):
#                 print(my_list[j],end="")
#                 print(my_list2[j],end="")
#                 print(my_list3[j],end="")
#                 print(my_list4[j],end="")
#                 print(my_list5[j])

#             if my_list2[9] != "x":
#                 my_list2[i] = "."


# # ////////////////my_list3
#             if my_list2[9] == "x":
#                 i = -1
#                 while True:
#                     sleep(1)
#                     Cls()
#                     i+=1
#                     my_list3[i] = "x"
#                     for j in range(len(my_list)):
#                         print(my_list[j],end="")
#                         print(my_list2[j],end="")
#                         print(my_list3[j],end="")
#                         print(my_list4[j],end="")
#                         print(my_list5[j])

#                     if my_list3[9] != "x":
#                         my_list3[i] = "."
                        
#                     if my_list3[9] == "x":
#                         break
#             # if my_list2[9] == "x":
#             #     break

# # ////////////////my_list4
#                 if my_list3[9] == "x":
#                     i = -1
#                     while True:
#                         sleep(1)
#                         Cls()
#                         i+=1
#                         my_list4[i] = "x"
#                         for j in range(len(my_list)):
#                             print(my_list[j],end="")
#                             print(my_list2[j],end="")
#                             print(my_list3[j],end="")
#                             print(my_list4[j],end="")
#                             print(my_list5[j])

#                         if my_list4[9] != "x":
#                             my_list4[i] = "."
                            
#                         if my_list4[9] == "x":
#                             break
#                 if my_list2[9] == "x":
#                     break


    # if my_list[9] == "x":
    #     break



