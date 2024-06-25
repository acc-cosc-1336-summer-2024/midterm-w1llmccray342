#write functions here, don't add input('') statements here!
def get_day_of_week(day):
    my_day = ""
    
    if day == 1:
        my_day = "Monday"
    elif day == 2:
        my_day = "Tuesday"
    elif day == 3:
        my_day = "Wednesday"
    elif day == 4:
        my_day = "Thursday"
    elif day == 5:
        my_day = "Friday"
    elif day == 6:
        my_day = "Saturday"
    elif day == 7:
        my_day = "Sunday"
    else:
        my_day = "Invalid Number"

    return my_day
