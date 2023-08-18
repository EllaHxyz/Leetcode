class Solution(object):
    def intToRoman(num):
        values = [1000,900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M','CM','D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'VI', 'I']
        roman = ""
        
        for i in range(len(values)):
            while num >= values[i]:
                roman += symbols[i]
                num -= values[i]
        return roman
        


    
'''you can create a mapping between integer values and their corresponding Roman numeral symbols. Then, iterate through the mapping in descending order and repeatedly subtract the largest possible value from the input integer while adding the corresponding Roman numeral symbol to the result.'''
