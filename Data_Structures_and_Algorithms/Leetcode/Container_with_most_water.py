'''
Given a bar plot defined with an array, output the container that can hold the most water
Want to maximize the width and height to maximize the volume of the water
'''
def max_area(height): 
    # start with 2 pointers - one at the very left and right
    # compute area with this max width 
    left_pointer_idx = 0
    right_pointer_idx = len(height) - 1
    left_pointer = height[left_pointer_idx]
    right_pointer = height[right_pointer_idx]
            
    area = abs((right_pointer_idx)-left_pointer_idx) * min(left_pointer, right_pointer)
    
    max_height = max(height)
    
    while True:
        # check if l or r pointer is larger, move the smaller one inwards 

        if left_pointer < right_pointer:
            # move left_pointer
            left_pointer_idx += 1
        else:    
            # move right_pointer
            right_pointer_idx -= 1

        if left_pointer_idx == right_pointer_idx:
            # reached the end of array
            break

        left_pointer = height[left_pointer_idx]
        right_pointer = height[right_pointer_idx]

        area = max(area, abs((right_pointer_idx)-left_pointer_idx) * min(left_pointer, right_pointer))   
    return area

if __name__ == "__main__":
    # Example   
    height = [1,8,6,2,5,4,8,3,7]
    area = max_area(height)
    print(area)

