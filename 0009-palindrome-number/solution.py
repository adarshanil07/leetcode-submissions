class Solution(object):
    def isPalindrome(self, x):
        num_string = str(x)
        reversed_string = self.reverse_string(num_string)
        
        if num_string == reversed_string:
            return True
        else:
            return False
    
    def reverse_string(self, string):
        stack = []
        for element in string:
            stack.append(element)
            
        reversed_string = ""
        while stack:
            reversed_string += stack.pop()
        return reversed_string
  
        
