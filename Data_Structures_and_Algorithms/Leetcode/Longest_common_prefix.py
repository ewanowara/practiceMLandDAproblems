class Solution(object):
    def longestCommonPrefix(self, strs):
        
        strs.sort()
                
        str_save = ''
        i = 0
                
        if len(strs) == 1:
            str_save = strs[0]
        elif strs[0] == '' or strs[0] == "": # check if the first word is empty
            str_save = ''
            i = len(strs)-1
        else:
            while i < len(strs)-1 :  
                word_i = strs[i] #"c"
                word_i2 = strs[i+1]  

                if str_save == '': # empty
                    j = min(len(word_i), len(word_i2)) 
                else:
                    j = len(str_save)  

                while j > 0:
                    if word_i[0:j] == word_i2[0:j]: # check if the whole word is contained, 
                        str_save = word_i[0:j] # temporary prefix
                        j = 0 

                    else:
                        j = j - 1
                        if j == 0: 
                            str_save = ''
                i = i + 1
                # if first word wasn't matched, quit
                if i > 0 and str_save == '':
                    break
        return str_save 