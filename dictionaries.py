# import time
# snacks = {'ashvik':'cheetos', 'brad':'fritos','rob':'cookies', 'may':'chocolate', 'maya':'candy'}  #<-- dictionary syntax
# # print (snacks)
# # print (snacks['ashvik']) <--- print a specific value in the dictionary with a given key(prints cheetos)
# # snacks['rob'] = 'cereal' <--- change a value of a specific key; changes robs snack to cereal
# # snacks['bob'] = 'brownies' <--- add a key value pair to the dictionary
# # print(snacks)
# # for n in snacks:
# #     time.sleep(1)
# #     print (snacks[n])

# for n in snacks:
#     print (n, "has", snacks[n])
# del snacks['brad']
# print(snacks)
# print(snacks.keys()) #<---- prints all the keys in the dictionary
# print(snacks.values()) #<---- prints all the values in the dictionary


# menu = {'bread': 5, 'cookies':10, 'chocolate':2, 'cake': 15, 'bagel': 5}
# for y in menu:
#     print (y, "---------- $", menu[y])
# a = input("What item would you like to purchase?: ")
# if a in menu:
#     print('The price is $', menu[a])
# else:
#     print("Try somewhere else.")

# fampw = {'amma':'123', 'appa':'1234', 'akka': '987', 'ashvik':'510'}
# tries = 3
# while tries != 0:
#     name = input("enter username: ")
#     if name in fampw:
#         pw = input("enter password: ")
#         if pw == fampw[name]:
#             print("access granted")
#             break
#         else:
#             print("incorrect password")
#             tries -= 1
#     else:
#         print ("no account found.")
#         tries -= 1
#     print ('You have', tries, "tries left.")

# qna = {'1+1': '2', 'what color is red': 'red', 'what color is water':'blue', '5+5':'10', 'can eggs be broken':'yes'}
# points = 0
# for n in qna:
#     answer = input(n+ ": ")
#     if answer == qna[n]:
#         print("right")
#         points += 1
#     else:
#         print ("wrong")
# print (points, "out of 5.")

nums = {1:'', 2:'', 3:'', 4:'', 5:''}
for n in nums:
    if n%2 == 0:
        nums[n] = n**2
    else:
        nums[n] = n/2
print (nums)