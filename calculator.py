# Import queue
from queue import Queue

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operators = ['+', '-', '*']


# Function that checks whether the string entered by the user is valid.
def check_validity(string):
    # Checks if there's an operator at the beginning or the end of the string.
    if string[0] in operators or string[len(string) - 1] in operators:
        return False

    # Boolean value for error checking
    operator_last = False
    for i in range(len(string)):
        if string[i] == ' ':
            # Loop that checks for double operators/operands separated by a space character
            for (j) in range(i+1, len(string)):
                if string[j] in digits:
                    if not operator_last:
                        return False
                    else:
                        break
                elif string[j] in operators:
                    if operator_last:
                        return False
                    else:
                        break
                elif string[j] == ' ':
                    continue
            continue
        operator_last = False
        if string[i] not in digits:
            operator_last = True
            if string[i] not in operators:
                return False
            # Check for double operators.
            elif string[i - 1] in operators or string[i + 1] in operators:
                return False
    return True


# Function that converts user input into a list of integers and operators
def convert_string_to_list(user_input):
    new_string = ""
    for i in range(len(user_input)):
        # Appends digits to the new string to be converted
        if user_input[i] in digits:
            new_string += user_input[i]
        # Adds a space before an after any operator for easy conversion
        elif user_input[i] in operators:
            new_string += ' ' + user_input[i] + ' '
    # Converts string to list, delimited by spaces
    return new_string.split()


def main():
    while True:
        print("Please input a infixed simple mathematical equation ")
        user_input = input()
        valid = check_validity(user_input)
        expression = convert_string_to_list(user_input)

        if not valid:
            print('Error: Invalid string.')

        else:
            print('valid')


if __name__ == "__main__":
    main()
