"""
for row in range(5):
    for column in range (5):
        print("(" + str(row) + ", " + str(column) + ")", end=' ')
print()


grades_keanu = [98, 90, 43, 87, 65]
student_summary = {"keanu": grades_keanu}
grades_setareh = [65, 87, 48, 85, 98]
student_summary["setareh"] = grades_setareh
for student, grades in student_summary.items():
    for grade in grades:
        if grade ==90:
            print(student + " earned an A+!")





def f():
    global x
    print("Within f: x =", x)
    x = 9
    print("Within f: x =", x)
x = 5
print("Before f: x =", x) # What gets printed?
f()
print("After f: x =", x) # What gets printed?


fave_langs = {'Chris': 'Python','Keanu':'Java', 'Kim': 'JavaScript'}
for name in sorted(fave_langs.keys()):
    print(name.title() + 'likes' + fave_langs[name])

for language in fave_langs.values():
    print(language.title())
"""

global_variable = 'global_variable'


def do_something(outer_parameter):
    local_variable_in_outer = 'local_variable_in_outer'
    global_variable = 'GLOBAL_VARIABLE'

    print(global_variable, outer_parameter, local_variable_in_outer)


def main():
    do_something(global_variable)
    print(global_variable)


if __name__ == "__main__":
    main()


student_name = 'N/A'

def get_name( ):
    global student_name
    name = 'Jessica'
    student_name = name

get_name( )
print('Student name: ', student_name)


def obfuscate(sequence, modifier):
    for index, _ in enumerate(sequence):
        sequence[index] = modifier(sequence[index])


def surprise(value):
    value *= 2


def main():
    collection = ['eye', 'heart', 'snake']
    obfuscate(collection, surprise)
    print(collection)


if __name__ == "__main__":
    main()

#4.
def num_triple(num):
    return num * 3
print(num_triple(4))

#5.
def distance(km):
    return km * 39370.1
print(distance(3))

#6
def average(a, b, c):
   return (a + b + c) / 3
print(average(0, 5, 2))

#7
def remove_min(a,b,c,d):
    orange = (a,b,c,d)
    list = sorted(orange)
    popped = list.pop(0)
    return list
print(remove_min(2,4,6,7))

def best_3(a,b,c,d):
    numbers = remove_min(a,b,c,d)
    return average(numbers[0], numbers[1], numbers[2])

#8
x = 3
print("the rabbit is", x)

#9
def total_length(s1, s2):
    """
    >>> total_length("yes", "no")
    5
    >>> total_length("yes", "")
    3
    >>> total_length("yes!!", "nooo")
    9
    """
    return len(s1) + len(s2)

#10
print(4 != 4.0)

#12
def different(a, b):
   return a != b
print(different(1,2))

#14
pH = 2
if 3 < pH < 7.0:
    print(pH, "is acidic")
elif pH < 3.0:
    print(pH, "is VERY acidic! Be careful.")

#15
pH = 3.6
if pH < 7.0:
    print(pH, "is acidic")
if pH < 4.0:
    print(pH, "is VERY acidic! Be careful.")
"""
#16
def exist(string):
    mycharacter = str(input("enter character: "))
    return string.find(mycharacter)
print(exist("hello"))

#17
def exist2(string):
    mycharacter = str(input("enter character: "))
    return string.count(mycharacter)
print(exist2("oh my god bro"))
"""

#18
s = " yes "
print(s.strip())

#20
list = [4353, 2314, 2956, 3382, 9362, 3900]
list.remove(3382)
print(list)
index = list.index(9362)
print(index)
list.insert(list.index(9362) + 1, 4499)
print(list)
list.append(5566)
list.append(1830)
print(list)
reverse_list = list.reverse()
print(list)
print(sorted(list))

#21
appointment = ["9:00", "10:30", "14:00", "15:00", "15:30"]
appointment.append("16:30")
print(appointment)
appointment = appointment + ["16:30"]
print(appointment)

#23
for x in range(0, 7):
    for y in range(0,x+1):
        print("T",end="")
    print("\r")

#24
for x in range(0, y+1):
    for y in range(0,7):
        print("T",end="")
    print("\r")

#25
def shape_inverse():
    t = 1
    spaces = 6
    for row in range(7):
        print(f'{" " * spaces}{"T" * t}', end='')

        t += 1
        spaces -= 1
        print()

#26
def find_duplicates(list_of_int):
    count = {}
    duplicates = []

    for element in lst:
        if element not in count.keys():
            count[element] = 1
        else:
            duplicates.append(element)

    return duplicates


lst = [1, 2, 3, 1, 2]
print(find_duplicates(lst))

#27
def count_values(dictionary: dict):
    return len(set(dictionary.values()))

"""x = 6
def f():
    print("Within f: x =", x)
    x = 12
    print("Within f: x =", x)
print("Before f: x =", x)
f()
print("After f: x =", x)"""

vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(list(vowel_tuple))



















