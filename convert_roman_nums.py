integers = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
def romanToInt(roman) -> str:
    result = 0
    for i, c in enumerate(roman):
        if i + 1 < len(roman) and integers[roman[i]] < integers[roman[i + 1]]:
            result -= integers[roman[i]]
        else:
            result += integers[roman[i]]
    return str(result)


print(romanToInt('IV'))