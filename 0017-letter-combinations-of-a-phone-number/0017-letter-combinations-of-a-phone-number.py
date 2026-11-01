class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        my_dict = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result = []
        letters = []
        for digit in digits:
            letters.append(my_dict[digit])
        if len(letters) == 1:
            for char in letters[0]:
                result.append(char)
        
        else:
            result = list(letters[0])
            for i in range(len(letters)-1):
                new_temp = []
                for char in result:
                    for chars in list(letters[i+1]):
                        new_temp.append(char+chars)
                result = new_temp

        return result
                




            



        