def reverse(self, x: int) -> int:
    if -(2 ** 31) <= x <= (2 ** 31) -1:
        i = 1
        ans = ""
        copy = abs(x)
        while copy > 0:
            ans += str(copy % 10)
            copy = copy // 10
        
        if len(ans) == 0:
            return 0
    
        ans = int(ans) if x > 0 else -(int(ans))
        if -(2 ** 31) <= ans <= (2 ** 31) -1:
            return ans
        
    return 0