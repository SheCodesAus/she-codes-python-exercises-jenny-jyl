# for loop

# my_iterable = [1, 2, 3]

# for item in my_iterable:
#     # some code here , doesnt have to be "item", can be anything
#     print(item)

# for num in range(10):
#     print(num)
# -- last number non inclusive

# from ast import Or


# Or for ranges

# for num in range(1, 10):
#     print(num)


# for steps/alternate numbers

# for num in range(1, 11, 2):
#     print(num)

# Challenge 1
# for num in range(101):
#     print(num)


# Challenge 2
# for num in range(0, 101, 5):
#     print(num)


# for letter in "Jenny":
#     print(letter)


# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]

# for item in range(len(chilli_wishlist)):
#     print(chilli_wishlist[item])

# for item in range(len(chilli_wishlist)-1):
#     print(chilli_wishlist[item])

# for item in chilli_wishlist:
#     print(item)

# Challenge 1

# for item in chilli_wishlist:
#     print(f"Chilli wants: {item}")

# chilli_wishlist = [["igloo"],
#                    ["donut toy", "tennis ball", "crocodile toy"],
#                    ["chicken", "peanut butter"],
#                    ["cardboard box", "kong", "dig mat"]]

# for category in chilli_wishlist:
#     for item in category:
#         print(item)

# While Loops

# some_boolean_condition = True
# while some_boolean_condition:
#     # do something
#     pass

# counter = 10

# while counter <= 10:
#     print(counter)
#     # -- ie. if counter is 10 or less, it will keep running this(infinite loop)
#     counter = counter + 1
#     # would '10' once (in first loop, is 10 but in second loop, becomes 11)
#     # instead of counter = counter + 1, can do counter +=1

# guess = ""
# while guess != "a":
#     guess = input("Guess a letter: ")

# if guess == "a":
#     print("You have guessed right!")

# Loops: For Loops

# Q1
# number = int(input("Choose a number: "))

# for x in range(0, number + 1):
#     output = number * x
#     print(f"{number} x {x} = {output}")


# Question 2
# number = int(input("Enter a number: "))

# result = 0

# for x in range(0, number + 1):
#     result = result + x

# print(result)

# Answer
# number = int(input("Enter a number: "))
# sum = 0
# for i in range(0, number+1):
#     sum = sum + i
# print(sum)


# Question 3
# random_numbers = [-3, -5, 9, 1]
# total = 0

# for i in range(len(random_numbers)):
#     total += random_numbers[i]

# print(total)


# mailing_list = [
#     ["Chilli", "chilli@thechihuahua.com"],
#     ["Roary", "roary@moth.catchers"],
#     ["Remus", "remus@kapers.dog"],
#     ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
#     ["Ivy", "noreply@goldendreamers.xyz"],
# ]

# for x in range(0, len(mailing_list)):
#     print(f" {mailing_list[x][0]} : {mailing_list[x][1]}")


# While Loops: Exercise

# Question 1


# from multiprocessing.connection import answer_challenge

# number = int(input("Enter a number: "))
# total = 0

# while number != "":
#     total = int(total) + int(number)
#     number = input("Enter a number: ")

# print(total)


# answer_challenge

# Question 2

# number = input("Enter a number: ")
# total = 0
# while i in range(0, number+1, 2)
#     total = total +

# Answer
# from ast import Or


# number = int(input("Enter a number: "))

# counter = 0
# while counter <= number:
#     if counter % 2 == 1:
#         print(counter)
#     counter += 1

# Or

# for i in range(1, number+1, 2)
#     print(i)


# Or


# while counter <= number:
#     print(counter)
#     counter += 2


# Question 3

# number = 4

# choice = int(input("Guess a number: "))

# while choice != number:
#     if choice > number:
#         print("too high")
#     else:
#         if choice < number:
#             print("too low")
#     choice = int(input("Guess a number: "))

# if choice == int(number):
#     print("you got it right!")


# Extension questions

# # Quesion 1

# groceries = [
#     ["Baby Spinach", 2.78],
#     ["Hot Chocolate", 3.70],
#     ["Crackers", 2.10],
#     ["Bacon", 9.00],
#     ["Carrots", 0.56],
#     ["Oranges", 3.08]
# ]

# bs_unit = float(input("How many baby spinach did you buy? "))
# groceries[0].append(bs_unit)

# hc_unit = float(input("How many hot chocolate did you buy? "))
# groceries[1].append(hc_unit)


# cracker_unit = float(input("How many crackers did you buy? "))
# groceries[2].append(cracker_unit)


# b_unit = float(input("How many bacons did you buy? "))
# groceries[3].append(b_unit)


# carrot_unit = float(input("How many carrots did you buy? "))
# groceries[4].append(carrot_unit)

# o_unit = float(input("How many oranges did you buy? "))
# groceries[5].append(o_unit)


# x = 0
# print("== == Izzy's Food Emporium == ==")
# for x in range(0, len(groceries)):
#     print(f"{groceries[x][0]}   {groceries[x][1]*groceries[x][2]}")


# # Question 2

# message = input("Please enter a string: ")
# x = 0
# for x in range(0, len(message)):
#     print(f"{x} {message[x]}")

# Question 3

# number = int(input("Pyramid size: "))

# i = 0
# for i in range(0, number+1):
#     print("*" * i)

# Question 4
# number = int(input("Pyramid size: "))
# i = 1
# for i in range(1, number+1, 2):
#     print(" "*int((number - int(i))/2) + "*" * int(i) + " "*int((number - int(i))/2))


# Scipt that buys things on Amazon until budget is used
import random  # random is a module that can randomise numbers
budget = 100  # dollars
how_much_spent = 0  # dollars


def buy_stuff():
    cost_of_item = random.randint(0, 20)
    return cost_of_item


how_much_spent = + buy_stuff()
print(f"total spent: {how_much_spent}")

# check if over budget
if how_much_spent < budget:
    how_much_spent = + buy_stuff()
    print(f"total spent: {how_much_spent}")

for i in range(0, 100):
    how_much_spent = + buy_stuff()
    print(f"total spent: {how_much_spent}")

    input("--------")
    if how_much_spent > budget:
        break

while how_much_spent < budget:
    how_much_spent = + buy_stuff()
    print(f"total spent: {how_much_spent}")

    input("--------")
