#Functions: block of code that performs a specific task
# Normal function
# Lambda function

##Normal functions >>
def hello():
    print("hello world!")
    return "hello world!"

def capitalize_hello():
    print(hello().capitalize())


hello()
capitalize_hello()

## Normal function with parameter
def greet_hello(person):
    print("Hello",person,"! How are you?")

greet_hello("Raman")

## Addition opertion with function and return
def sum_2_numbers(number_1, number_2):
    return number_1 + number_2

print(sum_2_numbers(2,10))

## Function to return even or odd
def even_or_odd(input):
    if input%2 == 0:
        return True
    else:
        return False

evaluate = int(input("Enter any number:"))      #must typecast input to int as default from input is str
print(type(evaluate))
match even_or_odd(evaluate):                    #match case > the equivalent of switch case statements (from Py3.10)
    case True:
        print("Number is even!")
    case False:
        print("Number is odd!")
    case _:
        print("The default option.")
    

#lambda functions >> Later from handbook
cube_of_number = lambda x:x*x*x                             #One-parameter lambda function
print("Cube of the number:",cube_of_number(evaluate))

mult_two_numbers = lambda x,y: x*y                          #Two-parameter lambda function
print("Multiplication of",evaluate,"and 9 is:",mult_two_numbers(evaluate,9))

#Filter, map and reduce: TODO>

