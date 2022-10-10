from queue import Queue

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operators = ['+', '-', '*']


# Function that checks whether the string entered by the user is valid.
def check_validity(list_equation):
    # Checks if there's an operator at the beginning or the end of the string.
    if list_equation[0] in operators or list_equation[len(list_equation)-1] in operators:
        return False

    for i in range(len(list_equation)-1):
        # Double operator check
        if list_equation[i] in operators and list_equation[i+1] in operators:
            return False
        # Check for invalid character (not digits or operators)
        elif not list_equation[i].strip('-').isnumeric() and not list_equation[i] in operators:
            return False
    return True


# Function that converts user input into a list of integers and operators
def convert_string_to_list(user_input):
    # Instantiates new string to be converted with delimiting space characters
    new_string = ""
    digit_last = False
    for i in range(len(user_input)):
        # Appends digits to the new string to be converted
        if user_input[i] in digits:
            new_string += user_input[i]
            digit_last = True
        elif user_input[i] in operators:
            # Negative number or subtraction operation check
            if user_input[i] == '-':
                if digit_last:
                    new_string += ' ' + user_input[i] + ' '
                    digit_last = False
                else:
                    for j in range(i+1, len(user_input)):
                        if user_input[j] in digits:
                            new_string += user_input[i]
                            digit_last = False
                            break
                        elif user_input[j] in operators:
                            return None
            # Adds space before and after operator for delimiting
            else:
                new_string += ' ' + user_input[i] + ' '
                digit_last = False
        # Double operand check
        elif user_input[i] == ' ':
            for j in range(i+1, len(user_input)):
                if user_input[j] in digits:
                    if digit_last:
                        return None
                    else:
                        break
                elif user_input[j] in operators:
                    break
        else:
            return None
    # Converts string to list, delimited by spaces
    return new_string.split()
    

# Function that implements basic calculator Logic
# parameters: toCalculate = A string of infixed valid operators and operands
def calculate(toCalculate):
    # Initialise a queue to evaluate the equation
    q = Queue(maxsize=0)

    # loop through the list and push operands and operators into a queue
    #   while evaluating multiplication operators
    i = 0
    while i < len(toCalculate):
        # if the element is an operator put it on the queue
        if toCalculate[i] in operators:
            q.put(toCalculate[i])

        # else it must be an operand so cast it as an int and put it on the stack
        else:
            swapped = False
            # if there is more than 1 character in the list
            if i + 1 < len(toCalculate):
                # if the next operator is multiplication evaluate it and put in on result on the queue
                #   and skip over the operators and operands used
                if toCalculate[i + 1] == '*':
                    q.put(int(toCalculate[i]) * int(toCalculate[i + 2]))
                    i = i + 2
                    swapped = True

            # if no multiplication was found
            if not swapped:
                q.put(int(toCalculate[i]))

        i += 1

    # initialise the result
    result = 0

    while not q.empty():
        # while the FIFO queue isn't empty get the first elements which will be
        #   either an operand or an operator
        element = q.get()

        # Checking for single element queues
        if not q.empty():
            # Dealing with the 2 other possible scenarios, an operator or an operand dequeued
            #   if the operator is a + add the operands, else it must be a minus so subtract them
            #   and add them to the result
            element2 = q.get()
            if element in operators:
                if element == "+":
                    result += element2
                else:
                    result -= element2
            else:
                element3 = q.get()
                if element2 == "+":
                    result += (element + element3)
                else:
                    result += (element - element3)
        else:
            result = element
    return result


def main():
    while True:
        print("Please input a infixed simple mathematical equation ")
        user_input = input()
        expression = convert_string_to_list(user_input)
        if expression is None:
            valid = False
        else:
            valid = check_validity(expression)

        if not valid:
            print('Error: Invalid string.')

        else:
            print('valid')
            print("result = " + str(calculate(expression)))


if __name__ == "__main__":
    main()
