def reverse(self, x: int) -> int:
    mini=int(str(abs(x))[::-1]) if x>0 else -int(str(abs(x))[::-1])
    return 0 if mini<(-2)**31 or mini>(2**31)-1 else mini