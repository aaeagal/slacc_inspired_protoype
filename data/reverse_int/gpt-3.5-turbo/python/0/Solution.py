import math

class Solution(object):
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


