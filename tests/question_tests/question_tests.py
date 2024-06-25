#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config, use_global
from src.question_b.question_b import get_random_number
from src.question_c.question_c import get_day_of_week
from src.question_d.question_d import get_assessment_value, get_tax_assessed


class Test_Config(unittest.TestCase):
  
  
    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_question_a_use_global(self):
        my_var = "fish"
        my_var = use_global()
    
        
        self.assertEqual(True, my_var == "Python")
    
    def test_question_b_get_random_number(self):
        test_var = get_random_number()

        self.assertEqual(False, test_var <= 0)
        self.assertEqual(True, test_var >= 1 and test_var <= 5)
        self.assertEqual(False, test_var > 6)

    def test_question_c_get_day_of_week(self):
        self.assertEqual(True, get_day_of_week(0) == "Invalid Number")
        self.assertEqual(True, get_day_of_week(1) == "Monday")
        self.assertEqual(True, get_day_of_week(2) == "Tuesday")
        self.assertEqual(True, get_day_of_week(3) == "Wednesday")
        self.assertEqual(True, get_day_of_week(4) == "Thursday")
        self.assertEqual(True, get_day_of_week(5) == "Friday")
        self.assertEqual(True, get_day_of_week(6) == "Saturday")
        self.assertEqual(True, get_day_of_week(7) == "Sunday")
        self.assertEqual(True, get_day_of_week(8) == "Invalid Number")

    def test_question_d_get_assessment_value(self):
        value1 = 10000
        value2 = 20000

        self.assertEqual(True, get_assessment_value(value1) == 6000)
        self.assertEqual(True, get_assessment_value(value2) == 12000)

    def test_question_d_get_tax_assessed(self):
       value1 = 6000
       value2 = 10000

       self.assertEqual(True, get_tax_assessed(value1) == 43.20)
       self.assertEqual(True, get_tax_assessed(value2) == 72)
        


