import math
class Solution(object):
    def reverse(self, x: int) -> int:
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