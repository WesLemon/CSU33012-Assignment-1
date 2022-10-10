# Import queue
from queue import Queue

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operators = ['+', '-', '*']


# Function that checks whether the string entered by the user is valid.
def check_validity(string):
    # Checks if there's an operators at the beginning or the end of the string.
    if string[0] in operators or string[len(string) - 1] in operators:
        return False

    for i in range(len(string)):
        # Checks to see if each character is a digit or an operator.
        if string[i] not in digits:
            if string[i] not in operators:
                return False
            # Check for double operators.
            elif string[i - 1] not in digits or string[i + 1] not in digits:
                return False
    return True


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

        # Dealing with the 2 possible scenarios, an operator or an operand dequeued
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

    return result


def main():
    while True:
        print("Please input a infixed simple mathematical equation ")
        expression = input()
        valid = check_validity(expression)

        if not valid:
        print('Error: Invalid string.')

        else:
        print('valid')
        print("result = " + str(calculate(expression)))


if __name__ == "__main__":
    main()
