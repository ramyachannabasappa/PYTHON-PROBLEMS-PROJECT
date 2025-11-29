class IntegerToRoman:
    def intToRoman(self, num: int) :
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syms[i]
                num -= val[i]
            i += 1
        return roman_num
    
#main():
if __name__ == "__main__":
    num = int(input("Enter an integer: "))
    object = IntegerToRoman()
    print(f"The Roman numeral representation of {num} is: {object.intToRoman(num)}")