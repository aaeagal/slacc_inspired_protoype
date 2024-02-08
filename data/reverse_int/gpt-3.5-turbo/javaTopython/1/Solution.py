import sys
class Solution:
    def reverse1(self, x: int) -> int:
        num = abs(x)
        rev = 0
        
        while num != 0:
            ld = num % 10

            # Overflow check
            if rev > (2147483647 - ld) // 10:
                return 0

            rev = rev * 10 + ld
            num = num // 10
            
        if x < 0:
            rev = -rev
            
        return rev


    def reverse2(x):
        num = abs(x)
        rev = 0
        
        while num != 0:
            ld = num % 10
            
            # Overflow check
            if rev > (2147483647 - ld) / 10:
                return 0
                
            rev = rev * 10 + ld
            num = num // 10
        
        if x < 1:
            rev = rev * (-1)
            
        return rev


    def reverse3(x):
        num = abs(x)
        
        rev = 0
        
        while num != 0:
            ld = num % 10
            
            # Overflow check
            if rev > (sys.maxsize - ld) // 10:
                return 0
            
            rev = rev * 10 + ld
            num = num // 10
        
        if x < 1:
            rev = rev * (-1)
        
        return rev

    def reverse4(self, x):
        num = abs(x)

        rev = 0

        while num != 0:
            ld = num % 10

            # Overflow check
            if rev > (2147483647 - ld) / 10:
                return 0

            rev = rev * 10 + ld
            num = num // 10

        if x < 1:
            rev = rev * (-1)
        return rev


    def reverse5(x):
        num = abs(x)
        rev = 0

        while num != 0:
            ld = num % 10

            # Overflow check
            if rev > (sys.maxsize - ld) / 10:
                return 0

            rev = rev * 10 + ld
            num = num // 10

        if x < 1:
            rev = rev * (-1)

        return rev


    def reverse6(x):
        num = abs(x)
        
        rev = 0
        
        while num != 0:
            ld = num % 10
            
            # Overflow check
            if rev > (pow(2,31) - 1 - ld) / 10:
                return 0
            
            rev = rev * 10 + ld
            num = num // 10
        
        if x < 1:
            rev = rev * (-1)
        return rev


    def reverse7(x):
        num = abs(x)
        
        rev = 0
        
        while num != 0:
            ld = num % 10
            
            # Overflow check
            if rev > (sys.maxsize - ld) / 10:
                return 0
            
            rev = rev * 10 + ld
            num = num // 10
        
        if x < 1:
            rev = rev * -1
        
        return rev


    def reverse8(x):
        num = abs(x)
        
        rev = 0
        
        while num != 0:
            ld = num % 10
            
            # Overflow check
            if rev > (sys.maxsize - ld) / 10:
                return 0
            
            rev = rev * 10 + ld
            num = num // 10
        
        if x < 1:
            rev = rev * (-1)
        
        return rev


    def reverse9(x):
        num = abs(x)
        
        rev = 0
        
        while num != 0:
            ld = num % 10
            
            # Overflow check
            if rev > (sys.maxsize - ld) // 10:
                return 0
            
            rev = rev * 10 + ld
            num = num // 10
        
        if x < 1:
            rev = rev * -1
        
        return rev


    def reverse10(self, x: int) -> int:
        num = abs(x)
        rev = 0

        while num != 0:
            ld = num % 10

            # Overflow check
            if rev > (sys.maxsize - ld) / 10:
                return 0

            rev = rev * 10 + ld
            num = num // 10
        
        if x < 0:
            rev = -rev
        
        return rev



    def reverse11(self, x: int) -> int:
        num = abs(x)
        
        rev = 0
        
        while num != 0:
            ld = num % 10
            
            # Overflow check
            if rev > (sys.maxsize - ld) // 10:
                return 0
            
            rev = rev * 10 + ld
            num = num // 10
        
        if x < 1:
            rev = rev * (-1)
        
        return rev



    def reverse12(self, x: int) -> int:
        num = abs(x)
        
        rev = 0
        
        while num != 0:
            ld = num % 10
            
            # Overflow check
            if rev > (sys.maxsize - ld) // 10:
                return 0
            
            rev = rev * 10 + ld
            num = num // 10
            
        if x < 1:
            rev = rev * (-1)
        
        return rev



    def reverse13(self, x):
        num = abs(x)
        
        rev = 0
        
        while num != 0:
            ld = num % 10
            
            # Overflow check
            if rev > (sys.maxsize - ld) / 10:
                return 0
            
            rev = rev * 10 + ld
            num = num // 10
        
        if x < 0:
            rev = -rev
        
        return rev


    def reverse14(x):
        num = abs(x)
        
        rev = 0
        
        while num != 0:
            ld = num % 10
            
            # Overflow check
            if rev > (sys.maxsize - ld) / 10:
                return 0
            
            rev = rev * 10 + ld
            num = num // 10
        
        if x < 1:
            rev = rev * (-1)
        return rev



    def reverse15(self, x: int) -> int:
        num = abs(x)
        rev = 0
        
        while num != 0:
            ld = num % 10
            
            # Overflow check
            if rev > (2147483647 - ld) // 10:  # Integer.MAX_VALUE is 2147483647 in Python
                return 0
            
            rev = rev * 10 + ld
            num = num // 10
        
        if x < 1:
            rev = rev * (-1)
        
        return rev


    def reverse16(x):
        num = abs(x)
        rev = 0
        
        while num != 0:
            ld = num % 10
            
            if rev > (sys.maxsize - ld) / 10:
                return 0
            
            rev = rev * 10 + ld
            num = num // 10
        
        if x < 1:
            rev = rev * (-1)
        
        return rev


    def reverse17(x):
        num = abs(x)
        rev = 0
        
        while num != 0:
            ld = num % 10
            
            # Overflow check
            if rev > (sys.maxsize - ld) / 10:
                return 0
            
            rev = rev * 10 + ld
            num = num // 10
            
        if x < 1:
            rev = rev * (-1)
            
        return rev


    def reverse18(x):
        num = abs(x)
        rev = 0

        while num != 0:
            ld = num % 10

            # Overflow check
            if rev > (2147483647 - ld) // 10:
                return 0

            rev = rev * 10 + ld
            num = num // 10
            
        if x < 1:
            rev = rev * -1
            
        return rev


    def reverse19(x):
        num = abs(x)
        
        rev = 0
        
        while num != 0:
            ld = num % 10
            
            # Overflow check
            if rev > (sys.maxsize - ld) / 10:
                return 0
            
            rev = rev * 10 + ld
            num = num // 10
        
        if x < 1:
            rev = rev * (-1)
        
        return rev

    def reverse20(self, x: int) -> int:
        num = abs(x)
        
        rev = 0
        
        while num != 0:
            ld = num % 10
            
            # Overflow check
            if rev > (2147483647 - ld) // 10:
                return 0
            
            rev = rev * 10 + ld
            num = num // 10
        
        if x < 1:
            rev = rev * -1
        
        return rev



