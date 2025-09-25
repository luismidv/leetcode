def romanToInt(s: str):
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res = 0
    last = 0

    for number in range(len(s)):
        current = romans[s[number]]
        if last < current:
            current -= last
            res-=last
            res += current
            last = current
        else:
            last = current
            res += current
        print(res)
    return res

print(romanToInt('XIV'))