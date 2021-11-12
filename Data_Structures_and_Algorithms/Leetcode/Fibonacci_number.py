# class Solution(object):
#     def fib(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         # base case
#         if n == 0 or n == 1:
#             return n
#         else:
#             return self.fib(n-1) + self.fib(n-2)

# more efficient with memoization 
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # base case    
        if n == 0 or n == 1:
            return n
        else:
            memo = [0] * (n + 1) # init empty array of length N + 1
            memo[1] = 1
            for i in range(2, n+1):
                memo[i] = memo[i-1] + memo[i-2]
            return memo[n] 


            