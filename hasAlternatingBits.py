def hasAlternatingBits(self, n: int) -> bool:
    if 1 <= n <= (2 ** 31) - 1:
        prevValue = -1
        while n > 0:
            remainder = n % 2
            if prevValue == remainder and prevValue >= 0:
                return False
            
            prevValue = remainder
            n = n // 2

        return True
    return False