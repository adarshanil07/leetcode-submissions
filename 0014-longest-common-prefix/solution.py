class Solution(object):
    def longestCommonPrefix(self, strs):
        
        
        prefix = ""

        minLength = self.returnMinLength(strs)

        if minLength == 0:
            return prefix


        letterIndex = 0
        currentLetter = strs[0][0]



        valid = True
        while valid == True:
            for word in strs:
                if word[letterIndex] == currentLetter:
                    valid = True
                else:
                    return prefix
                
            prefix += currentLetter

            letterIndex += 1

            if letterIndex >= minLength:
                return prefix

            
            currentLetter = strs[0][letterIndex]

            

    
    def returnMinLength(self, strs):
        minLength = len(strs[0])
        for word in strs:
            if len(word) < minLength:
                minLength = len(word)

        return minLength
        
