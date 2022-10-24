import math

def eratosthenes(upper_bound):
    """
    """
    number_list = []
    result = []
    for number in range(2, upper_bound + 1):
        number_list.append(number)

    counter = 0
    while counter < math.sqrt(upper_bound):
        for x in number_list:
            if x % number_list[counter] == 0 and x != number_list[counter]:
                number_list.pop(number_list.index(x))
        counter += 1
    print(number_list)

print(eratosthenes(30))