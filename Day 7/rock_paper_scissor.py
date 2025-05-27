import random

def computer_choice():
    return random.choice(['Rock','Paper','Scissor'])

def user_choice():
       choice=input("Enter rock,paper or scissor: ").lower()
       while choice not in['rock','paper','scissor']:
         print("Invalid choice!,Try again")
         choice=input("Enter rock,paper or scissor: ").lower()
         return choice
def decide_winner(user,computer):
    if user ==computer:
        print("It's a tie")
    elif(user=='rock'and computer =='scissor') or(user=='scissor' and computer=='paper') or(user=='paper' and computer=='rock'):
        print("you win")
    else:
     return "Computer wins"

def play():

    print("=== Rock,Paper,Scissor Game ===")
    while True:
        user=user_choice()
        computer=computer_choice()
        print(f"you chose {user}")
        print(f"Computer chose  {computer}")
        print(decide_winner(user,computer))

        play_again=input("Do you want to play ?(yes/no")
        if play_again=='no':
            print("Thank you for playing!")
            break
play()
