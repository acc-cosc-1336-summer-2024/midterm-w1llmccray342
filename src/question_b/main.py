#add import
import question_b

def main_menu():
    keep_running = "y"

    while keep_running == "y":
        

        print("Would you like to keep running?")
        keep_running = input("Y to keep running or any other button to stop")

        keep_running = keep_running.lower()

def game():
    question_b.get_random_number()



def main():
    pass