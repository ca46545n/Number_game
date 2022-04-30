import random

def number_game():
    print("=====================Welcome to the Number Guessing Game====================")
    print("            Rules  ")
    print("1. Your guess can not be no larger than 10!")
    print("2. The game will end when you guess incorrectly!!!")
    print("3. For every Answer you get right you will gain 10 points ")
    print("4. Have Fun!! ")

    score = 0
    answers_right = 0
    attempts = 5

    while attempts > 0:

        computer_choice = random.randint(0, 10)
        print(f"Computer's choice: {computer_choice}")
        gamer_choice = int(input("Enter a number between 0 and 10: "))
        attempts = attempts - 1
        print(f"{attempts} attempts left")
        print(gamer_choice)

        if gamer_choice > 10:
            print("sorry that is to high of a number you need to try again.")

        elif computer_choice == gamer_choice:
            score += 10
            answers_right += 1
            if score == 50:
                print(f"Congrats!!! you won! your SCORE is {score} You got all {answers_right} answers right! ")
                break
            print(f"Congrats you have chosen the correct number {computer_choice} you current score is {score}")


        else:
            print("sorry that is not correct!")
            print(f"The computer's choice was: {computer_choice}")
            print(f"GAME OVER! Final score is {score}. You got {answers_right} answers right")
            break

    decision = input("Would you like to play a new game?")

    if decision.lower() == "yes" or decision.lower() == "y":
        number_game()

    elif decision.lower() == "no" or decision.lower() == "n":
        print("Bye, Thanks for playing! ")


if __name__ == "__main__":
    number_game()
