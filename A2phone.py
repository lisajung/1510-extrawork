"""
Lisa Jung
A01332998
"""

number = {"A": 2, "B": 2, "C": 2, "D": 3, "E": 3, "F": 3, "G": 4, "H": 4, "I": 4, "J": 5, "K": 5, "L": 5, "M": 6, "N": 6, "O": 6, "P": 7, "Q": 7, "R": 7,
          "S": 7, "T": 8, "U": 8, "V": 8, "W": 9, "X": 9, "Y": 9, "Z": 9}
def string_to_list(string):
    """
    >>> string_to_list("hello")
    ['h', 'e', 'l', 'l', 'o']
    >>> string_to_list("555-GET-FOOD")
    ['5', '5', '5', '-', 'G', 'E', 'T', '-', 'F', 'O', 'O', 'D']
    """
    return list(string)

def phone(string):
    """
    Translate alphabetic phone numbers to their numerical equivalent.

    :param string: a string
    :precondition: string must be in the format XXX-XXX-XXXX where each X is alphanumeric
    :postcondition: translate alphabetic number into a numerical number equivalent
    :return: numeric number as a string
    >>> phone("555-GET-FOOD")
    '555-438-3663'

    """
    result = ""
    for digit in string:
        if digit in number:
            result += str(number[digit])
        else:
            result += str(digit)
    return result


    result = ""
    string_as_list = list(string)
    while string_as_list != []:
        if string_as_list[0] in number:
            result += str(number[string_as_list[0]])
            string_as_list.pop(0)
        else:
            result += string_as_list[0]
            string_as_list.pop(0)
    return result
