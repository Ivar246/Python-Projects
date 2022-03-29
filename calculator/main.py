from replit import clear
def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1,n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2

"""mapping operator with operation"""
operator= {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    f_num = float(input('Enter first number: '))
    for i in operator:
         print(i)

    is_exit = False
    while not is_exit:
        operation_symbol = input('select the operator: ')
        s_num = float(input('Enter next number: '))

        operation = operator[operation_symbol]
        result = operation(f_num, s_num)
        print(f'{f_num} {operation_symbol} {s_num} = {result}')

        user_choice = input("Type 'Y' to continue calculation and 'R' to restart and 'N' to exit:")
        if user_choice.upper() == 'Y':
            f_num = result
        elif user_choice.upper() == 'R':
            is_exit = True
            clear()
            calculator()
        else:
            is_exit =True

            
calculator()
