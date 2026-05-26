
# # # # Intro to for loops

# # # # for n in range(0, 10, 1):
# # # #     print ("Hello")

# # # for n in range(1, 11, 1):
# # #     print (n)

# # for n in range(0, 100, 1):
# #     print (n, "Ashvik")

# for n in range(1, 21, 1):
#     if n%2 == 0:
#         print(n, "even")
#     else:
#         print (n, "odd")

# countdown

# import time
# time1 = int(input("Where should we start?: "))
# for n in range(time1, 0, -1):
#     print (n)
#     time.sleep(1)
# print ("Blast Off!")
    
    
# y = int(input("Which number?: "))
# for n in range(0, 13, 1):
#     print ( y, "*", n, " = ", y * n)


# printing on the same line

# print ("Hello", end=" ")
# print ("World")

# *****
# for n in range (0, 5, 1):
#     print ("*", end=" ")
    
# 11111
# 22222
# 33333
# 44444
# 55555    
# for y in range (1, 6, 1):
#     for n in range (1, 6, 1):
#         print (y, end=" ")
#     print ()    
        
# *
# **
# ***
# ****        
# for n in range (0, 5, 1):
#     for y in range (0, n, 1):
#         print ("*", end=" ")
#     print ()   


# ****
# ***
# **
# *
# for n in range (4, 0, -1):
#     for y in range (0, n, 1):
#         print ("*", end=" ")
#     print ()

# for n in range (100, 0, -3):
#     if n > 20 and n < 30:
#         print ("Tick Tock")
#     else:
#         print (n)

# for n in range (2, 9, 2):
#     for y in range (9, n, -2):
#         print (y, end="")
#     print ()

# import random
# num = 0
# for n in range (0, 20, 1):
#     y = round(random.uniform(1, 10), 2)
#     num = num + y
#     print (y)
    
# print (round(num, 2))

# import random
# y = random.randint(1, 100)
# for n in range (1, y, 1):
#     print (n)