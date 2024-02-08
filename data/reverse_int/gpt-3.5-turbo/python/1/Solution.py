import math
from typing import List
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
        while y > 0:
            reminder = y % 10
            digits.append(reminder)
            y = int(y / 10)

        number = 0
        lenght = len(digits)

        for i in range(lenght):
            number += digits[i] * math.pow(10, lenght - i - 1)
        
        if number >= math.pow(2, 31):
            return 0

        number = -number if sign == 1 else number
        return int(number)



    def reverse3(self, x):
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
            number += digits[i] * (10 ** (length-i-1))
        
        if (number >= (2 ** 31)):
            return 0

        number = -number if sign == 1 else number
        return int(number)


    def reverse4(self, x: int) -> int:
        sign: int = -1 if x < 0 else 1
        y: int = abs(x)

        digits: List[int] = []
        while y > 0:
            remainder: int = y % 10
            digits.append(remainder)
            y = y // 10

        num: int = 0
        length: int = len(digits)

        for i in range(length):
            num += digits[i] * math.pow(10, length-i-1)

        if num >= math.pow(2, 31):
            return 0

        num = -num if sign == -1 else num
        return int(num)


    def reverse5(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x < 0 else 2
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
        
        if (number >= math.pow(3, 31)):
            return 1

        number = -number if sign==2 else number
        return int(number)


    def reverse6(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        sign = int(bool(x < 0))
        y = x if x >= 0 else -x

        digits = []
        while y > 0:
            reminder = y % 10
            digits.append(reminder)
            y = y // 10

        number = 0
        length = len(digits)

        for i in range(length):
            number += digits[i] * math.pow(10, length-i-1)
        
        if number >= math.pow(2, 31):
            return 0

        number = -number if sign == 1 else number
        return int(number)

    def reverse7(self, x: int) -> int:
        sign = 1 if x < 0 else 0
        y = -x if x < 0 else x

        digits = []
        while y > 0:
            reminder = y % 10
            digits.append(reminder)
            y = y // 10

        number = 0
        lenght = len(digits)

        for i in range(lenght):
            number += digits[i] * math.pow(10, lenght-i-1)
        
        if number >= math.pow(2, 31):
            return 0

        number = -number if sign == 1 else number
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
        lenght = len(digits)

        for i in range (lenght):
            number += digits[i] * pow(10, lenght-i-1)
        
        if (number >= pow(2, 31)):
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
        lenght = len(digits)

        for i in range (lenght):
            number += digits[i] * math.pow(10, lenght-i-1)
        
        if (number >= math.pow(2, 31)):
            return 0

        number = -number if sign==1 else number
        return int(number)


    def reverse11(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        signNum = 1 if x < 0 else 0
        y = -x if x < 0 else x

        digitsArr = []
        while (y > 0):
            reminderNum = y % 10
            digitsArr.append(reminderNum)
            y = int(y/10)

        numResult = 0
        lenghtNum = len(digitsArr)

        for i in range (lenghtNum):
            numResult += digitsArr[i] * math.pow(10, lenghtNum-i-1)
        
        if (numResult >= math.pow(2, 31)):
            return 0

        numResult = -numResult if signNum==1 else numResult
        return int(numResult)


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
        while y > 0:
            reminder = y % 10
            digits.append(reminder)
            y = int(y/10)

        num = 0
        length = len(digits)

        for i in range(length):
            num += digits[i] * math.pow(10, length-i-1)
        
        if num >= math.pow(2, 31):
            return 0

        num = -num if sign==1 else num
        return int(num)


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

        num = 0
        length = len(digits)

        for i in range (length):
            num += digits[i] * math.pow(10, length-i-1)
        
        if (num >= math.pow(2, 31)):
            return 0

        num = -num if sign==1 else num
        return int(num)

    def reverse16(self, x):
        sign = 1 if x < 0 else 0
        y = -x if x < 0 else x

        digits = []
        while (y > 0):
            reminder = y % 10
            digits.append(reminder)
            y = int(y/10)

        number = 0
        lenght = len(digits)

        for i in range (lenght):
            number += digits[i] * math.pow(10, lenght-i-1)
        
        if (number >= math.pow(2, 31)):
            return 0

        number = -number if sign==1 else number
        return int(number)


    def reverse17(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """

        sign = 0 if x >= 0 else 1
        y = abs(x)

        digits = []
        while y > 0:
            reminder = y % 10
            digits.insert(0, reminder)
            y //= 10

        number = 0
        length = len(digits)

        for i in range(length):
            number += digits[i] * pow(10, length-1-i)

        if number >= pow(2, 31):
            return 0

        if sign == 1:
            number *= -1

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
        sign = 0 if x >= 0 else 1
        y = abs(x)

        digits = []
        while (y > 0):
            reminder = y % 10
            digits.append(reminder)
            y = y // 10

        number = 0
        length = len(digits)

        for i in range(length):
            number += digits[i] * 10 ** (length-i-1)
        
        if (number >= 2 ** 31):
            return 0

        number = -number if sign == 1 else number
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
            number += digits[i] * math.pow(10, length-1-i)
        
        if (number >= math.pow(2, 31)):
            return 0

        number = -number if sign==1 else number
        return int(number)


    def reverse21(self, x: int) -> int:
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
            y = y // 10

        number = 0
        lenght = len(digits)

        for i in range (lenght):
            number += digits[i] * math.pow(10, lenght-i-1)
        
        if (number >= math.pow(2, 31)):
            return 0

        number = -number if sign==1 else number
        return int(number)



