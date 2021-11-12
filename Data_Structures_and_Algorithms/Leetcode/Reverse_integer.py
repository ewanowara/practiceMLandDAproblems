class Solution(object):
    def reverse(self, x):
        
        rev_x = 0
        
        if x >= 0: # positive
            sign = + 1      
        elif x < 0: # negative
            sign = -1
            x = x * sign # remove sign for now
        
        while x > 0:
            rev_x = rev_x * 10 + x % 10
            x = x/10
        
        # check if output is within 32 bit bounds
        if rev_x <= (-2**31) or rev_x >= (2**31):
            rev_x = 0
        print(rev_x*sign)    
        return rev_x*sign # restore the sign
        