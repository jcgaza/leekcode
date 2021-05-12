def bitwiseComplement(self, N: int) -> int:
    if N == 0:
        return 1
    
    ceil = 0
    copy_N = N
    while copy_N > 0:
        ceil += 1
        copy_N = copy_N // 2
    
    ceil = (2 ** ceil) - 1
    return ceil - N