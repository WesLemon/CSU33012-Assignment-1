import calculator_gui

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operators = ['+', '-', '*']


# Function that checks whether the string entered by the user is valid.
def check_validity(list_equation):
    # Checks if there's an operator at the beginning or the end of the string.
    if list_equation[0] in operators or list_equation[len(list_equation) - 1] in operators:
        return False

    for i in range(len(list_equation) - 1):
        # Double operator check
        if list_equation[i] in operators and list_equation[i + 1] in operators:
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
                    for j in range(i + 1, len(user_input)):
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
            for j in range(i + 1, len(user_input)):
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


def calculate():
    pass
    # TODO


def main():
    calculator = calculator_gui.GUI()


if __name__ == "__main__":
    main()
