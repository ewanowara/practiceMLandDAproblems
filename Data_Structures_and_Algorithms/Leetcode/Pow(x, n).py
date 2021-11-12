class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        result = 1 
        if n > 0:
            while n > 0:
                result = result*x
                n = n - 1
            return result
        
        elif n == 0:
            return 1
        elif n < 0:
            while n < 0:
                result = result*x
                n = n + 1
            return (1/result)