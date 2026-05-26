#a = ["apple", "banana", "blueberry", "raspberry", "mango"]   #<---list format
# print (a)
# a.append("grape")    #<---- add to the list
# print (a)
# print (a[0])  #<---- print apple (1st thing on the list = 0)
# r = a.pop(2)     #<----remove blueberry and store it in r ; without a nunber in the parenthesis, it will remove the last index position
# print (r)
# a.insert(1, "orange")  #<--- add orange to index position 1 on the list
# print (a)
# a.remove("raspberry") #<--- remove a specific item on the list (in this case, raspberry)
# print (a)
# a.reverse()  #<--- reverse the list
# print (a)
# a.sort()   #<--- sorts it alphabetically. If a number is used inside the parenthesis, will sort numerically. if a.sort(reverse = 1),
#                                                                                                             # reverse sorts alphabetically.
# print (a)

# for n in range(0, len(a), 1):  <--- looping through list using index position
#     print (a[n])

# for n in a:          <---- alternate way to loop through list using a
#     print (n)

# names = ["Brad", "Chad", "Matt", "Crad", "Lad"]
# print (len(names))   #<--prints how many index positions there are
# print (names[1:])    #<--prints the list starting from index position 1
# names[2] = "Sam"     #<--replaces index position 2 with Sam
# print (names)
# names.insert(2, "Rob")
# names.append("Randy")
# print (names)
# names.pop(4)
# print (names)
# names.remove("Rob")
# names.pop(2)
# print (names)
# names.sort(reverse=1)
# print (names)
# r = names[:]
# print (r)
# r.sort()
# print (names, r)

# for n in range(0, len(names), 1):
#     print (names[n])

# for a in r:
#     print(a)

# r = "hello world"
# l = r.split()     # <----by word
# print (l)
# a = list(r)      # <--- by character
# print (a)
# print ("".join(a))

# a = "Oliver"
# c = []
# while True:
#     b = input("Enter the code name: ")
#     if b == a:
#         print ("Access Granted.")
#         print ("Wrong Passwords tried ", c)
#         break
#     else:
#         c.append(b)
#         print ("Access Denied")

# import random
# d = []
# a = []
# for n in range(0, 21, 1):
#     r = random.randint(1, 100)
#     d.append(r)
# d.sort()
# print (d)
# for n in range(0, len(d), 1):
#     if d[n] > 20:
#         a.append(d[n])
# print (a[1])
# print (a[len(a)-2])
# print (a)
# for y in range(0, 11, 1):
#     random.shuffle(a)
# print (a[0])

# import random
# n = ["batman", "superman", "dexter", "iron man", "harry potter"]
# selected = random.sample(n, 2)  <---picks random samples.
# print (selected)


# import random
# l = []
# for n in range(0, 10, 1):
#     y = random.randint(1, 200)
#     if y%7 == 0:
#         l.append(y)
# print (l)



# a = ["apple", "banana", "blueberry", "raspberry", "mango"]
# for n in a:
#     if "a" in n: <---- if can also be used to see if a letter is in a variable/fraction of a list
#         print(n)

# import random
# h = ["basketball", "volleyball", "working out", "soccer", "football"]
# p = ["doctor", "lawyer", "astronaut", "engineer", "computer engineer"]
# a = ["15", "20", "40", "60", "80"]
# print("John likes to do ", random.choice(h), " and wants to become a ", random.choice(p), " when he grows up. He is ", random.choice(a), " years old.")

# y = []   
# l = ['ball', 'cat', 'dog', 'hut', 'brick', 'pot', 'whip', 'box', 'fade', 'tub']
# for n in l:
#     y.append(len(n))
# print (y)

# letter = input("Pick a letter: ")
# for n in l:
#     if letter in n:
#         print (n)
#     for x in range(0, len(n), 1):
#          if letter in n[x]:
#             print (x)
            
# import random

# a = random.choice(l)
# f = a
# a = list(a)
# random.shuffle(a)
# a = ("".join(a))
# print (a)
# y = input("What word was it?: ")
# if y == f:
#     print ("correct")
# else:
#     print ("incorrect")
    
# l = ['ford', 'dude', 'gay', 'hi', 'james', 'yo', 'optimal', 'pedigree', 'house', 'big']

# for n in range(len(l)-1, -1, -1):
#     if n%2 == 0:
#         l.pop(n)
# print (l) 

# l = ['1', '2', '3', '4', '5', '6']
# for n in range(0, len(l), 1):
#     print (l[n], end="")
#     if n == 2:
#         print()


# num = int(input("Pick a number: "))
# l = []
# for n in range (1, num+1, 1):
#     l.append(n)
# for y in range(0, len(l), 1):
#     if y == len(l)//2:
#         print()
#     print (l[y], end="")


# import random
# l=[]
# for n in range(0, 5, 1):
#     y = random.randint(0, 10)
#     l.append(y)
# h = []
# for n in l:
#     d = n * 2
#     h.append(d)
# print (l)
# print (h)

# billMarks = [86, 80, 78, 94]
# TomMarks = [65, 78, 79, 87]
# MikeMarks = [89, 76, 87, 75]

# h = []
# h.append(billMarks)
# h.append(TomMarks)
# h.append(MikeMarks)
# print (h)
# print (h[1][2])
# answer = input("Pick a subject: ")
# if answer == "math":
#     i = 0
# if answer == "writing":
#     i = 1
# if answer == "history":
#     i = 2
# if answer == "Science":
#     i = 3  
# # print (round((h[1][i] + h[2][i] + h[0][i])/3, 2))

# w = [[90, 100, 110, 120], [140, 230, 123, 125], [123, 153, 124, 212], [143, 153, 165, 240]]
# for n in range(0, 4, 1):
#     for x in range(0, len(w[n]), 1):
#         print ("person ", n+1 , " had ",w[x][n] , " weight in year ", x+1)
#     print()

# import random
# l = ["hi", "bye", "cry", "food", "random", "eager", "washing", "machine"]
# strikes = 5
# d = random.choice(l)
# d = list(d)
# r = []
# for g in d:
#     r.append("_")
# print (d)
# print (r)
# while strikes>0:
#     letter = input("Pick a letter: ")
#     if letter in d:
#         for n in range(0, len(d), 1):
#             if letter == d[n]:
#                 r[n] = d[n]
#     else:
#         strikes -= 1
#         print("incorrect, you have ", strikes, " chances.")
#     print(r)
#     if r == d:
#         print("correct!")
#         break

items = [['muffins', 'bread', 'cake', 'cookies', 'bagel'], [5, 10, 10, 5, 10]]
cart = []
total = 0
for n in range(0, 5, 1):
    print (items[0][n], "   -   $", items[1][n])
while True:
    cc = input("Pick an item: ")
    while cc not in items[0]:
        print("Invalid Input.")
        cc = input("Pick an item: ")
    cart.append(cc)
    confirmation = input("Is there anything else you would like to order?: ")
    while confirmation not in ['yes', 'no']:
        print ("Invalid Input.")
        confirmation = input("Is there anything else you would like to order?: ")
    if confirmation == "yes":
        continue
    elif confirmation == "no":
        break
print ("BILL")
for y in cart:
    f = items[0].index(y)
    total += items[1][f]
    print (y, "--", "$", items[1][f])
print ("Total   ---   $", total)

