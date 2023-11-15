#Write a python program that takes an input 5 from user and then type cast those values to string, int and float in the separate variables. Print all the variables.
# Taking 5 inputs from the user
input1 = input("Enter the first value: ")
input2 = input("Enter the second value: ")
input3 = input("Enter the third value: ")
input4 = input("Enter the fourth value: ")
input5 = input("Enter the fifth value: ")

# Typecasting to string, int, and float
string_var = str(input1), str(input2), str(input3), str(input4), str(input5)
int_var = int(input1), int(input2), int(input3), int(input4), int(input5)
float_var = float(input1), float(input2), float(input3), float(input4), float(input5)

# Printing the variables
print("\nString variables:", string_var)
print("Integer variables:", int_var)
print("Float variables:", float_var)
