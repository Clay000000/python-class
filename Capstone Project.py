import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()."

# string = lower + upper + numbers + symbols
# length = 10
# password = "".join(random.sample(string,length))
# print("Your new password is: " + password)

def generate_pw (select):
    if select == "a":
        string = lower + upper + numbers + symbols
        length = 10
        password = "".join(random.sample(string,length))

    elif select == "b":
        string = lower + upper + numbers + symbols
        length = 15
        password = "".join(random.sample(string,length))

    elif select == "c":
        string = lower + upper + numbers + symbols
        length = 20
        password = "".join(random.sample(string,length))

    
    print("Your new password is: " + password)

print("Welcome to Password Generator! ")
print("How long would you like your password to be?     A: 10 characters,     B: 15 characters,     C: 20 characters")
userselection = input("").lower()
while userselection not in ["a", "b", "c" ]:
    print("That is not in the list. Please pick A, B, or C.")
    userselection=input("").lower()

generate_pw(userselection)




print("If you would you like another password, How long would you like your password to be?     A: 10 characters,     B: 15 characters,     C: 20 characters.")


def second_pass (select):
    if select == "y":
        print("How long would you like your password to be?     A: 10 characters,     B: 15 characters,     C: 20 characters")
userselection = input("").lower()
while userselection not in ["a", "b", "c" ]:
    print("That is not in the list. Please pick A, B, or C.")
    userselection=input("").lower()

generate_pw(userselection)



print("If you would you like another password, How long would you like your password to be?     A: 10 characters,     B: 15 characters,     C: 20 characters.")                                                                                                                                                                                                                                                           


def second_pass (select):
    if select == "y":
        print("How long would you like your password to be?     A: 10 characters,     B: 15 characters,     C: 20 characters")
userselection = input("").lower()
while userselection not in ["a", "b", "c" ]:
    print("That is not in the list. Please pick A, B, or C.")
    userselection=input("").lower()

generate_pw(userselection)



print("If you would you like another password, How long would you like your password to be?     A: 10 characters,     B: 15 characters,     C: 20 characters.")

# I got really confused on how to make the second password optioin, but this worked, I know its a little weird.

def second_pass (select):
    if select == "y":
        print("How long would you like your password to be?     A: 10 characters,     B: 15 characters,     C: 20 characters")
userselection = input("").lower()
while userselection not in ["a", "b", "c" ]:
    print("That is not in the list. Please pick A, B, or C.")
    userselection=input("").lower()

generate_pw(userselection)
print("                                                                                                                                                                                                                                                                                ")
print("                                                                                                                                                                                                         Your free passcode generator trial has ended. Please upgrade your plan.")
print("                                                                                                                                                                                                         Thank you for using my password generator, see you soon!")
print("                                                                                                                                                                                                                                                                                ")