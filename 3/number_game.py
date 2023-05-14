import random
guess_number = random.randint(1,101)
print("----> > Welcome to the number Guessing game using python < < ----")
user_number = int(input("Enter the number of your choice : "))
while True:
    if user_number > guess_number:
        user_number = int(input("Your Guess number is higher \n Enter lower number \n ::--> "))
    elif user_number < guess_number:
        user_number = int(input("Your Guess number is lower \n Enter higher number \n ::--> "))
    else:
        print("Congratulation You Guess the right number")
        print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
        break