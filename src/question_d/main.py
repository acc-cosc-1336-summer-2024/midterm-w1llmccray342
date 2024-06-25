#add import

import question_d


# Code is reusable
def user_input():
    user_flt_input = float(input("Please enter any value: "))
    user_assess_val = question_d.get_assessment_value(user_flt_input)
    user_tax_assess = question_d.get_tax_assessed(user_assess_val)

    print("Your assessment value of the property is...", user_assess_val)
    print("Your property tax is...", user_tax_assess)

def main_menu():
    keep_running = "y"

    while keep_running == "y":
        
        user_input()

        print("Would you like to try again with a different property?")
        keep_running = input("Y to keep running or any other button to stop: ")

        keep_running = keep_running.lower()

        if keep_running != "y":
            print("See you next time!")

def main():
    main_menu()
    
main()