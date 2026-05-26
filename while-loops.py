# intro to while loops


# y = -20
# while y <= 20:
#     print (y)
#     y = y+1


# y = -17
# while y < 25:
#     print (y)
#     y += 1
# while y > 8:
#     print (y)
#     y -= 1
# print ("hit")

#  y -= 1 -> y = y - 1
#  y += 1 -> y = y + 1
# import time
# import random
# c = 0
# while True:
#     print (random.randint(1, 10))
#     print (random.uniform(1, 10))
#     c += 1
#     time.sleep(2)
#     if c == 10:
#         break

#   countdown timer

# import time
# y = int(input("How long would you like your countdown to be?: "))

# while y >= 0:
#     print (y)
#     time.sleep(1)
#     y -= 1
# print ("boom")

# import random
# import time

# y = int(input("How much money would you like to deposit in your account?: "))
# while True:
#     if y == 0:
#         print ("Insufficient account balance.")
#         break
#     a = input("Would you like to roll the dice?: ")
#     if a == "Yes":
#         dice1 = random.randint(1, 6)
#         dice2 = random.randint(1, 6)
#         print ("Waiting for a few seconds.")
#         time.sleep(2)
#         if dice1 == dice2:
#             print ("You won!")
#             y += 5
#             print ("Current Account Balance: ", y)
#         else:
#             print ("You lost.")
#             y -= 1
#             print ("Current Account Balance: ", y)
#     else:
#         print ("Thank you for playing.")
#         break
    
# n = 0
# while n <= 50:
#     print (n)
#     n += 7
    
#  password
# pw = ("abc")
# while True:
#     d = input("What is the password?: ")
#     if d == pw:
#         print ("Access Granted.")
#         break
#     else:
#         print("Access Denied.")

# import random
# answ = random.randint(1, 10)
# tries = 1
# while True:
#     y = int(input("Pick a number: "))
#     if y == answ:
#         print("Correct.")
#         print ("You took ", tries, " tries.")
#         break
#     else:
#         print ("Wrong. This was try #", tries, ".")
#         tries += 1
#         if answ > y:
#             print ("Higher")
#         else:
#             print ("Lower")
#         if tries > 3:
#             print ("Game over.")
#             print ("The answer was: ", answ)
#             break

# import random
# while True:
#     y = random.randint(1, 100)
#     print (y)
#     if y == 88:
#         break
#     elif y%7 == 0 and y%9 == 0:
#         continue
#     elif y%7 == 0:
#         break
#     elif y%9 == 0:
#         break



# 11111
# 22222
# 33333

# d = 1
# while d<4: 
#     n = 1
#     while n<6:
#         print(d, end="")
#         n += 1
#     print ()
#     d += 1

# *
# **
# ***
# ****
# *****

d = 1
while d<5: 
    n = 1
    while n<d+1:
        print("*", end=" ")
        n += 1
    print ()
    d += 1