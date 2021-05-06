def romanToInt(self, s: str) -> int:
    if 1 <= len(s) <= 15:
        reverse = s[::-1]
        num = 0
        prevValue = ""
        for char in reverse:
            if char == "I":
                if prevValue == "X" or prevValue == "V":
                    num -= 1
                else:
                    num += 1
                prevValue = "I"
            elif char == "V":
                num += 5
                prevValue = "V"
            elif char == "X":
                if prevValue == "L" or prevValue == "C":
                    num -= 10
                else:
                    num += 10
                prevValue = "X"
            elif char == "L":
                num += 50
                prevValue = "L"
            elif char == "C":
                if prevValue == "D" or prevValue == "M":
                    num -= 100
                else:
                    num += 100
                prevValue = "C"
            elif char == "D":
                num += 500
                prevValue = "D"
            elif char == "M":
                num += 1000
                prevValue = "M"
        
        return num
    return 0