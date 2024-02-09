import math
import sys
def reverse1(self, x: int) -> int:
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x < 0 else 0
    y = -x if x < 0 else x

    digits = []
    while (y > 0):
        reminder = y % 10
        digits.append(reminder)
        y = int(y/10)

    number = 0
    length = len(digits)

    for i in range (length):
        number += digits[i] * math.pow(10, length-i-1)
    
    if (number >= math.pow(2, 31)):
        return 0

    number = -number if sign==1 else number
    return int(number)


def reverse2(self, x: int) -> int:
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x < 0 else 0
    y = -x if x < 0 else x

    digits = []
    while (y > 0):
        reminder = y % 10
        digits.append(reminder)
        y = int(y/10)

    number = 0
    length = len(digits)

    for i in range (length):
        number += digits[i] * math.pow(10, length-i-1)
    
    if (number >= math.pow(2, 31)):
        return 0

    number = -number if sign==1 else number
    return int(number)



def reverse3(self, x: int) -> int:
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x < 0 else 0
    y = -x if x < 0 else x

    digits = []
    while (y > 0):
        reminder = y % 10
        digits.append(reminder)
        y = int(y/10)

    number = 0
    length = len(digits)

    for i in range (length):
        number += digits[i] * math.pow(10, length-i-1)
    
    if (number >= math.pow(2, 31)):
        return 0

    number = -number if sign==1 else number
    return int(number)


def reverse4(self, x: int) -> int:
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x < 0 else 0
    y = -x if x < 0 else x

    digits = []
    while (y > 0):
        reminder = y % 10
        digits.append(reminder)
        y = int(y/10)

    number = 0
    length = len(digits)

    for i in range (length):
        number += digits[i] * math.pow(10, length-i-1)
    
    if (number >= math.pow(2, 31)):
        return 0

    number = -number if sign==1 else number
    return int(number)


def reverse5(self, x: int) -> int:
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x < 0 else 0
    y = -x if x < 0 else x

    digits = []
    while (y > 0):
        reminder = y % 10
        digits.append(reminder)
        y = int(y/10)

    number = 0
    length = len(digits)

    for i in range (length):
        number += digits[i] * math.pow(10, length-i-1)
    
    if (number >= math.pow(2, 31)):
        return 0

    number = -number if sign==1 else number
    return int(number)

def reverse6(self, x: int) -> int:
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x < 0 else 0
    y = -x if x < 0 else x

    digits = []
    while (y > 0):
        reminder = y % 10
        digits.append(reminder)
        y = int(y/10)

    number = 0
    length = len(digits)

    for i in range (length):
        number += digits[i] * math.pow(10, length-i-1)
    
    if (number >= math.pow(2, 31)):
        return 0

    number = -number if sign==1 else number
    return int(number)


def reverse7(self, x: int) -> int:
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x < 0 else 0
    y = -x if x < 0 else x

    digits = []
    while (y > 0):
        reminder = y % 10
        digits.append(reminder)
        y = int(y/10)

    number = 0
    length = len(digits)

    for i in range (length):
        number += digits[i] * math.pow(10, length-i-1)
    
    if (number >= math.pow(2, 31)):
        return 0

    number = -number if sign==1 else number
    return int(number)

def reverse8(self, x: int) -> int:
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x < 0 else 0
    y = -x if x < 0 else x

    digits = []
    while (y > 0):
        reminder = y % 10
        digits.append(reminder)
        y = int(y/10)

    number = 0
    length = len(digits)

    for i in range (length):
        number += digits[i] * math.pow(10, length-i-1)
    
    if (number >= math.pow(2, 31)):
        return 0

    number = -number if sign==1 else number
    return int(number)

def reverse9(self, x: int) -> int:
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x < 0 else 0
    y = -x if x < 0 else x

    digits = []
    while (y > 0):
        reminder = y % 10
        digits.append(reminder)
        y = int(y/10)

    number = 0
    length = len(digits)

    for i in range (length):
        number += digits[i] * math.pow(10, length-i-1)
    
    if (number >= math.pow(2, 31)):
        return 0

    number = -number if sign==1 else number
    return int(number)

def reverse10(self, x: int) -> int:
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x < 0 else 0
    y = -x if x < 0 else x

    digits = []
    while (y > 0):
        reminder = y % 10
        digits.append(reminder)
        y = int(y/10)

    number = 0
    length = len(digits)

    for i in range (length):
        number += digits[i] * math.pow(10, length-i-1)
    
    if (number >= math.pow(2, 31)):
        return 0

    number = -number if sign==1 else number
    return int(number)

def reverse11(self, x: int) -> int:
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x < 0 else 0
    y = -x if x < 0 else x

    digits = []
    while (y > 0):
        reminder = y % 10
        digits.append(reminder)
        y = int(y/10)

    number = 0
    length = len(digits)

    for i in range (length):
        number += digits[i] * math.pow(10, length-i-1)
    
    if (number >= math.pow(2, 31)):
        return 0

    number = -number if sign==1 else number
    return int(number)

def reverse12(self, x: int) -> int:
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x < 0 else 0
    y = -x if x < 0 else x

    digits = []
    while (y > 0):
        reminder = y % 10
        digits.append(reminder)
        y = int(y/10)

    number = 0
    length = len(digits)

    for i in range (length):
        number += digits[i] * math.pow(10, length-i-1)
    
    if (number >= math.pow(2, 31)):
        return 0

    number = -number if sign==1 else number
    return int(number)

def reverse13(self, x: int) -> int:
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x < 0 else 0
    y = -x if x < 0 else x

    digits = []
    while (y > 0):
        reminder = y % 10
        digits.append(reminder)
        y = int(y/10)

    number = 0
    length = len(digits)

    for i in range (length):
        number += digits[i] * math.pow(10, length-i-1)
    
    if (number >= math.pow(2, 31)):
        return 0

    number = -number if sign==1 else number
    return int(number)

def reverse14(self, x: int) -> int:
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x < 0 else 0
    y = -x if x < 0 else x

    digits = []
    while (y > 0):
        reminder = y % 10
        digits.append(reminder)
        y = int(y/10)

    number = 0
    length = len(digits)

    for i in range (length):
        number += digits[i] * math.pow(10, length-i-1)
    
    if (number >= math.pow(2, 31)):
        return 0

    number = -number if sign==1 else number
    return int(number)

def reverse15(self, x: int) -> int:
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x < 0 else 0
    y = -x if x < 0 else x

    digits = []
    while (y > 0):
        reminder = y % 10
        digits.append(reminder)
        y = int(y/10)

    number = 0
    length = len(digits)

    for i in range (length):
        number += digits[i] * math.pow(10, length-i-1)
    
    if (number >= math.pow(2, 31)):
        return 0

    number = -number if sign==1 else number
    return int(number)

def reverse16(self, x: int) -> int:
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x < 0 else 0
    y = -x if x < 0 else x

    digits = []
    while (y > 0):
        reminder = y % 10
        digits.append(reminder)
        y = int(y/10)

    number = 0
    length = len(digits)

    for i in range (length):
        number += digits[i] * math.pow(10, length-i-1)
    
    if (number >= math.pow(2, 31)):
        return 0

    number = -number if sign==1 else number
    return int(number)

def reverse17(self, x: int) -> int:
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x < 0 else 0
    y = -x if x < 0 else x

    digits = []
    while (y > 0):
        reminder = y % 10
        digits.append(reminder)
        y = int(y/10)

    number = 0
    length = len(digits)

    for i in range (length):
        number += digits[i] * math.pow(10, length-i-1)
    
    if (number >= math.pow(2, 31)):
        return 0

    number = -number if sign==1 else number
    return int(number)

def reverse18(self, x: int) -> int:
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x < 0 else 0
    y = -x if x < 0 else x

    digits = []
    while (y > 0):
        reminder = y % 10
        digits.append(reminder)
        y = int(y/10)

    number = 0
    length = len(digits)

    for i in range (length):
        number += digits[i] * math.pow(10, length-i-1)
    
    if (number >= math.pow(2, 31)):
        return 0

    number = -number if sign==1 else number
    return int(number)

def reverse19(self, x: int) -> int:
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x < 0 else 0
    y = -x if x < 0 else x

    digits = []
    while (y > 0):
        reminder = y % 10
        digits.append(reminder)
        y = int(y/10)

    number = 0
    length = len(digits)

    for i in range (length):
        number += digits[i] * math.pow(10, length-i-1)
    
    if (number >= math.pow(2, 31)):
        return 0

    number = -number if sign==1 else number
    return int(number)

def reverse20(self, x: int) -> int:
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x < 0 else 0
    y = -x if x < 0 else x

    digits = []
    while (y > 0):
        reminder = y % 10
        digits.append(reminder)
        y = int(y/10)

    number = 0
    length = len(digits)

    for i in range (length):
        number += digits[i] * math.pow(10, length-i-1)
    
    if (number >= math.pow(2, 31)):
        return 0

    number = -number if sign==1 else number
    return int(number)


def main():
    if sys.argv[1] == "reverse1":
        print(reverse1(int(sys.argv[2])))
    elif sys.argv[1] == "reverse2":
        print(reverse2(int(sys.argv[2])))
    elif sys.argv[1] == "reverse3":
        print(reverse3(int(sys.argv[2])))
    elif sys.argv[1] == "reverse4":
        print(reverse4(int(sys.argv[2])))
    elif sys.argv[1] == "reverse5":
        print(reverse5(int(sys.argv[2])))
    elif sys.argv[1] == "reverse6":
        print(reverse6(int(sys.argv[2])))
    elif sys.argv[1] == "reverse7":
        print(reverse7(int(sys.argv[2])))
    elif sys.argv[1] == "reverse8":
        print(reverse8(int(sys.argv[2])))
    elif sys.argv[1] == "reverse9":
        print(reverse9(int(sys.argv[2])))
    elif sys.argv[1] == "reverse10":
        print(reverse10(int(sys.argv[2])))
    elif sys.argv[1] == "reverse11":
        print(reverse11(int(sys.argv[2])))
    elif sys.argv[1] == "reverse12":
        print(reverse12(int(sys.argv[2])))
    elif sys.argv[1] == "reverse13":
        print(reverse13(int(sys.argv[2])))
    elif sys.argv[1] == "reverse14":
        print(reverse14(int(sys.argv[2])))
    elif sys.argv[1] == "reverse15":
        print(reverse15(int(sys.argv[2])))
    elif sys.argv[1] == "reverse16":
        print(reverse16(int(sys.argv[2])))
    elif sys.argv[1] == "reverse17":
        print(reverse17(int(sys.argv[2])))
    elif sys.argv[1] == "reverse18":
        print(reverse18(int(sys.argv[2])))
    elif sys.argv[1] == "reverse19":
        print(reverse19(int(sys.argv[2])))
    elif sys.argv[1] == "reverse20":
        print(reverse20(int(sys.argv[2])))
    else:
        print("Invalid function name")
if __name__ == "__main__":
    main()