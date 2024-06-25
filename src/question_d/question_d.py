#write functions here, don't add input('') statements here!

def get_assessment_value(value):
    assessment_value = value * .60
    return assessment_value

def get_tax_assessed(value):
    
    necessary_assessment = value / 100

    tax_assessed = necessary_assessment *0.72

    return tax_assessed