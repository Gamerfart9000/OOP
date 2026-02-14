class RomanNumerals:
    _roman_map = [
        (1000, 'M'), (900, 'CM'),
        (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'),
        (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'),
        (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    @classmethod
    def int_to_roman(cls, num):
        if not 1 <= num <= 3999:
            raise ValueError("Number must be between 1 and 3999")

        result = []
        for value, symbol in cls._roman_map:
            count = num // value
            result.append(symbol * count)
            num -= value * count

        return ''.join(result)

    
@classmethod
def roman_to_int(cls, s: str) -> int:
        roman_dict = dict(cls._roman_map)
        i = 0
        total = 0
        
        while i < len(s):
            # Check two-character symbol first (e.g., CM, IV)
            if i + 1 < len(s) and s[i:i+2] in roman_dict:
                total += roman_dict[s[i:i+2]]
                i += 2
            else:
                total += roman_dict[s[i]]
                i += 1
        
        return total

o = RomanNumerals()


number = int(input("Enter a number to convert to Roman numeral: "))


print(f"The Roman numeral for {number} is: {o.int_to_roman(number)}")