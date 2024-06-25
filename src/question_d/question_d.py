#write functions here, don't add input('') statements here!

def get_assessment_value(value):
    assessment_value = value * .60
    return assessment_value

def get_tax_assessed(value):
    
    # Write a for loop for this:
    # Nested for loop maybe?

    tax_assessed = 0

    # For each $100 of assessment value increment by 72c 

    for values in range(0, len(value)):
        # If a value in the range of 0 to max value is 100 we increment the tax_assessed value by 72cents if not we do nothing.
        if values % 100 == 0:
            tax_assessed += 0.72
    return tax_assessed