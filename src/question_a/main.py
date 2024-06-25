#add import
import question_a

#Create a global variable and gather input from the user
global_var = input("Please enter any word, letter, or number: ")

#Input is stored into memory.

#Call question_a.use_global() and assign that value to global_var
global_var = question_a.use_global()

#Print expected output; this should return modifiedVar in question.a instead of input listed in global_var
print(global_var)
