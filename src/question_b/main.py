#add import
import question_b


def game():

    hidden_number = question_b.get_random_number

    my_guess = input("Please enter any number 1-5: ")

    while my_guess != hidden_number:

        if my_guess == hidden_number:
            print("You win!")
            return

        elif my_guess != hidden_number: 
            print("Try again")
    

def main_menu():
    keep_running = "y"

    while keep_running == "y":
        
        game()

        print("Would you like to play again?")
        keep_running = input("Y to keep running or any other button to stop")

        keep_running = keep_running.lower()

        if keep_running != "y":
            print("See you next time!")




def main():
    main_menu()