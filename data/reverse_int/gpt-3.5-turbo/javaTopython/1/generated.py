class Solution:
    def reverse(self, x: int) -> int:
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


def reverse(x):
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


def reverse(x):
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


class Solution:
    def reverse(self, x):
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


def reverse(x):
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


def reverse(x):
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


def reverse(x):
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


def reverse(x):
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


def reverse(x):
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


class Solution:
    def reverse(self, x: int) -> int:
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


class Solution:
    def reverse(self, x: int) -> int:
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


class Solution:
    def reverse(self, x: int) -> int:
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


class Solution:
    def reverse(self, x):
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


def reverse(x):
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


class Solution:
    def reverse(self, x: int) -> int:
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


def reverse(x):
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


def reverse(x):
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


def reverse(x):
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


def reverse(x):
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


```python
class Solution:
    def reverse(self, x: int) -> int:
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
```


