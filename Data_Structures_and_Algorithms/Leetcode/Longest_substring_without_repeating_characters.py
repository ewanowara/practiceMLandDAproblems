class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        chars = [None] * 128 # ASCII

        left = right = 0

        res = 0
        while right < len(s): # while have not reached the end of the string 
            r = s[right] # take the right element of string s
            
            index = chars[ord(r)] # converts a character into its Unicode code value
            if index != None and index >= left and index < right: # ?
                left = index + 1 # move forward
                
            res = max(res, right-left+1) # ?
            
            chars[ord(r)] = right # assign character
            right += 1 # move forward
        return res