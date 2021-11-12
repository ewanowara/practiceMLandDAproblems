class Solution(object):
    def romanToInt(self, s):
        
        hash_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        total_number = 0
        i = 0
        while i < len(s): 
            # subtractive case - at least 2 elements remain 
            if (i + 1 < len(s)) and (hash_values[s[i]] < hash_values[s[i+1]]):
                print('first case')
                total_number = total_number + hash_values[s[i+1]] - hash_values[s[i]] 
                i = i+2 # processed two elements
            # other
            else:
                print('second case')
                total_number = total_number + hash_values[s[i]]
                i = i+1 # processed two elements
                
        return total_number
            
            