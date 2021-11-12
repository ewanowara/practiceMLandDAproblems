class Solution(object):
    def isPalindrome(self, x):
        
        rev_int = 0

        if x == 0: # if 0 - it is a palindrome
            return True
        
        elif x < 0: # if negative it is not a palindrome
            return False
        else:   
            x_str = str(x) # convert to a string and check if the first and last element are the same 
            for i in range(len(x_str)):                    
                if x_str[i] != x_str[-i-1]:  # compare first and last element
                    # as soon as the elements are not equal, break and output False
                    return False    
                    break
            return True