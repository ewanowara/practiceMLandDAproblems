class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        def winner(nums,s,e,turn):
            
            if s == e: # if nums is a single element                
                return turn*nums[s] 
            
            a = turn * nums[s] + winner(nums, s+1, e, -turn) # change the sign of turn
            b = turn * nums[e] + winner(nums, s, e-1, -turn) # change the sign of turn
            
            return turn*max(turn*a, turn*b)
          
        return winner(nums, 0, len(nums)-1, 1) >= 0