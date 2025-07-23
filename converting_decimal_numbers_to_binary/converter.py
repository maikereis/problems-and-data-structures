from stack.stack import Stack

def divide_by_two(number):
    rem_stack = Stack()

    while number > 0:
        rem = number % 2
        rem_stack.push(rem)
        number = number // 2

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())
    
    return bin_string

def base_converter(number, base):
    digits = "0123456789ABCDEF"

    rem_stack = Stack()

    while number > 0:
        rem = number % base
        rem_stack.push(rem)
        number = number // base
    
    number_string = ""
    while not rem_stack.is_empty():
        number_string = number_string + digits[rem_stack.pop()]
    
    return number_string