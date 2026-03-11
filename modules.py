# time


# # import time

# # wrd = input("Enter a word: ")
# # print("Wait for 3 seconds.")
# # # time.sleep(3)
# # # if len(wrd) > 6:
# # #     print ("word is longer than six letters.")
# # # else:
# # #     print ("word is less than six letters.")

# # import time
# # print ("Server is busy, wait 5 seconds.")
# # time.sleep(5)
# # y = input("Would you like to refresh the page?: ")
# # if y == "Yes":
# #     print ("Please wait, your page is loading.")
# #     time.sleep(2)
# #     print ("There is high traffic. Please try again later.")
# # else:
# #     print ("Thank you for visiting our website.")


# random number

# import random
# num = random.randint(1,30)
# if num%2 == 0 and num% 3 == 0:
#     print (num)
# else:
#     print ("The number is not divisible by 2 and 3.")
    
# random integer
    
# import time
# import random
# # num = random.uniform(100, 1000)
# # print (num)
# # print ("Rounding up to 2 decimal places")
# # time.sleep(3)
# # print (round(num, 2))

# import random
# y = int(input("Pick a number of digits: "))
# x = (10**(y-1))
# z = (10**y)-1    
# num = random.randint(x, z)
# print (num)

# # math

# # import math

# # y = math.sqrt(25)  <- square roots
# # print (math.pi)


# import math
# laps = int(input("How many laps did you run today?: "))

# c = round((2 * (math.pi) * 100) * laps, 3)


# # print ("You have run", c, " meters today.")

# # import webbrowser
# # webbrowser.open_new_tab('youtube.com')

# webbrowser stuff

# import webbrowser
# y = input("What store would you like to buy from?: ")

# if y == "samsung":
#     webbrowser.open("samsung.com")
# elif y == "apple":
#     webbrowser.open("apple.com")
# else:
#     print ("Not available.")

# calendar stuff

# import calendar
# year = int(input("What year were you born in?: "))
# print (calendar.calendar(year))

# import calendar
# year = int(input("What year were you born in?: "))
# month = int(input("What month were you born in?: "))
# day = int(input("What day were you born on?: "))

# y = (calendar.weekday(year, month, day))

# if y == 0:
#     print ("Monday.")
# elif y == 1:
#     print ("Tueday")
# elif y == 2:
#     print ("Wednesday")
# elif y == 3:
#     print ("Thursday")
# elif y == 4:
#     print ("Friday")
# elif y == 5:
#     print ("Saturday")
# elif y == 6:
#     print ("Sunday")

import datetime
# print (datetime.datetime.now())

print (datetime.date.today())

