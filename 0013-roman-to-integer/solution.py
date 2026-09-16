class Solution(object):
    def romanToInt(self, s):
        
        numeral_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        numeral_list = []
        number_list = []
        total = 0

        for numeral in s:
            numeral_list.append(numeral)

        for numeral in numeral_list:
            number_list.append(numeral_dict[numeral])


       
        j = len(numeral_list) - 1
        i = j - 1


        while i > -1 and j > -1:

            if number_list[i] >= number_list[j]:
                total += number_list[j]

                i -= 1
                j -= 1

            elif number_list[i] < number_list[j]:
                val = number_list[j] - number_list[i]
                total += val

                i -= 2
                j -= 2

        if j == 0:
            total += number_list[j]
        return total
                
        
