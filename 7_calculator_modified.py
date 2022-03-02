from numpy import False_


print("Welcome to the CALCULATOR")


def add(first,second):
        return first + second

def sub(first,second):
        return first - second  

def mul(first,second):
        return first * second

def div(first,second):
        return first / second

ops = {
    '+' : add,
    '-': sub,
    '*': mul,
    '/': div
    }
def calculator():
    num1 = float(input("What is the first number: "))
    for key in ops:
        print(key) 
    end_calc = False

    while not end_calc: 
        op_choice = input("Please choose a operation from the list above: ")
        num2 = float(input("What is the next number: ")) 
        calc = ops[op_choice]
        answer = calc(num1,num2)

        print(f"{num1} {op_choice} {num2} = {answer}")
        
        ex = input(f"Type 'y' to keep calculating with {answer}, 'n' to start a new calculation or 'e' to exit: ")

        if ex == 'y':
            num1 = answer
        elif ex == 'n':
            calculator()
        elif ex == 'e':
            end_calc = True
            print("Goodbye")

calculator()










