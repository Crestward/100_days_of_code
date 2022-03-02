print("Welcome to the CALCULATOR")


op = ('''
    +
    -
    *
    /
    ''')


def operations(first, second, calc):
    if calc == '+' :
        ans = first + second
        return f"{first} {calc} {second} = {ans}"
    elif calc == '-' :
        ans = first - second
        return f"{first} {calc} {second} = {ans}"
    elif calc == '*' :
        ans = first * second
        return f"{first} {calc} {second} = {ans}"
    elif calc == '/' :
        ans = first / second
        return f"{first} {calc} {second} = {ans}"

end_calc = False

while not end_calc:
    first_number = int(input("What is the first number: "))
    print(op)
    operation = input("Pick an operation: ")
    second_number = int(input("What is the next number: "))
    
    answer1 = operations(first=first_number, second=second_number, calc=operation)
    
    print(answer1)

    cont = input("Type 'y' to continue calculating or type 'n' to stop: ")

    if cont == 'n':
        end_calc = True
        print('Goodbye')
