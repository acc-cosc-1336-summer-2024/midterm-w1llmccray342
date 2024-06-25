#write functions here, don't add input('') statements here!

def get_assessment_value(value):
    assessment_value = value * .60
    return assessment_value

def get_tax_assessed(value):
    tax_assessed = 0

    for values in range(value):
        if values % 100 == 0:
            tax_assessed += 0.72

    return round(tax_assessed, 2)

