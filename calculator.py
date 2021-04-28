"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


#add loop
while True:
    #read user input string
    user_input = input("Enter your math problem: ") #pow 3 5
    #create token = input_string.split(' ')
    tokens = user_input.split(' ') # => ['pow', '3', '5']
    #variable for math operators
    operator = tokens[0]
    #create a return variable
    result = None

    #if first token is "q":
    if "q" in tokens:
        print("Exiting...")
        break
    #else: 

    #variable for numbers
    num1 = tokens[1]
    num2 = tokens[2]
    
    #math functions
    #if token = "pow" then call power function
    if operator == "pow":
        result = power(float(num1), float(num2))

    print(result)
                
