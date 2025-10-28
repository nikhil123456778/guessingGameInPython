#this is a gussing game which will guess a number between 1 to 100
import random   
# number_to_guess=random.randint(1,100)
# guess=None
# while(guess!=number_to_guess):
#     guess=int(input("enter your guess between. 1 to 100:"))
#     if(guess<number_to_guess):
#         print("too low")
#     elif(guess>number_to_guess):
#         print("too high")
#     else:
#         print("you guessed it right!")  
# print(f"the number to guess was {number_to_guess}")
# print("you wanna play again? (y/n)")
# play_again=input()
# if(play_again=='y' or play_again=='Y'):
#     number_to_guess=random.randint(1,100)
#     guess=None
#     while(guess!=number_to_guess):
#         guess=int(input("enter your guess between. 1 to 100:"))
#         if(guess<number_to_guess):
#             print("too low")
#         elif(guess>number_to_guess):
#             print("too high")
#         else:
#             print("you guessed it right!")  
#     print(f"the number to guess was {number_to_guess}")
#     print("thank you for playing")


def play_game():
    while True:
        number_of_rounds = int(input("Enter the number of rounds you want to play (1–9): "))
        if number_of_rounds <= 0:
            print("Invalid input. Please enter a positive number.")
        elif number_of_rounds >= 10:
            print("Please choose less than 10 rounds.")
        else:
            print(f"You have chosen to play {number_of_rounds} rounds.")
            break
    
    while True:
        number_of_attempts=int(input("enter the number of attempts you want in each round:"))

        if(number_of_attempts<=0):
            print("invalid input")
            
        elif(number_of_attempts>10):
            print("please choose less than or equal to 10 attempts")
            
        else:  
            print(f"you have chosen to have {number_of_attempts} attempts in each round")
            break
    
    for round in range(1,number_of_rounds+1):
        print(f"round {round} starts now!")
        number_to_guess=random.randint(1,100)
        attempts_left=number_of_attempts
        while(attempts_left>0):
            guess=int(input("enter your guess between. 1 to 100:"))
            if(guess<number_to_guess):
                print("too low")
            elif(guess>number_to_guess):
                print("too high")
            else:
                print("you guessed it right!")  
                break
            attempts_left-=1
            print(f"attempts left: {attempts_left}")
        if(attempts_left==0):
            print(f"sorry! you've used all your attempts. the number was {number_to_guess}")
    print("thank you for playing")
play_game()


    
        