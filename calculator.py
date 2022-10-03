digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operators = ['+', '-', '*']


# Function that checks whether the string entered by the user is valid.
def check_validity(string):

    # Checks if there's an operators at the beginning or the end of the string.
    if string[0] in operators or string[len(string)-1] in operators:
        return False

    for i in range(len(string)):
        # Checks to see if each character is a digit or an operator.
        if string[i] not in digits:
            if string[i] not in operators:
                return False
            # Check for double operators.
            elif string[i-1] not in digits or string[i+1] not in digits:
                return False
    return True


def main():
    while True:
        expression = input()
        valid = check_validity(expression)

        if not valid:
            print('Error: Invalid string.')

        else:
            print('valid')
            # TODO


if __name__ == "__main__":
    main()
