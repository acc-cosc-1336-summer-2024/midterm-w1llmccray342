#add import
import question_c

# Code is reusable
def user_input():
    user_int_input = int(input("Please type in a number from 1-7: "))

    print(question_c.get_day_of_week(user_int_input))

def main_menu():
    keep_running = "y"

    while keep_running == "y":
        
        user_input()

        print("Would you like to enter another number?")
        keep_running = input("Y to keep running or any other button to stop: ")

        keep_running = keep_running.lower()

        if keep_running != "y":
            print("See you next time!")

def main():
    main_menu()
    
main()
