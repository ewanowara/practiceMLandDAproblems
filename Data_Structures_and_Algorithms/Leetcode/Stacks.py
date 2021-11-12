'''
Implement a stack class and use it to check if the parenthesis are balanced in an array or not 
'''
class MyStack():
    # 0th element is the bottom
    # -1th element is the top - the most recent
    def __init__(self):
        self.myStack = []

    def isempty(self): # check if stack is empty
        return self.myStack == [] 

    def push(self, item): # add a new element to the top
        self.myStack.append(item)
    
    def pop(self): # remove the element on top
        return self.myStack.pop() # automatically removes the last element
    
    def peak(self): # return the element on top but do not remove it
        return self.myStack[len(self.myStack) - 1]

    def size(self):
        return len(self.myStack)

    def display(self):    
        print(self.myStack)

'''
Example:
-- balanced

(((((((((())))))))))

-- unbalanced

((((((((((((()))))))

'''

def matches(open_c, close_c, open_characters, close_characters):
    return open_characters.index(open_c) == close_characters.index(close_c)

def check_balanced(bracket_array):

    if len(bracket_array) <= 0: # input is empty
        return False 
    else:    
        stack = MyStack()
        open_characters = '([{'
        close_characters = ')]}'
        for i in range(len(bracket_array)):
            if bracket_array[i] in open_characters:
                stack.push(bracket_array[i])
            elif bracket_array[i] in close_characters: # check if the next character is a closing bracket or a different character 
                if stack.isempty():
                    return False
                else:
                    top = stack.pop() 
                # check if the top character matches the correct shape of bracket
                if not matches(top, bracket_array[i], open_characters, close_characters):   
                    return False # if not, then not balanced    

    return stack.isempty()

if __name__ == "__main__":
    # Example   
    bracket_array = '((((((((((((()))))))'
    print(check_balanced(bracket_array))
