'''
Given an input image, output its integral image - replace each pixels value by the sum of all pixels above it and to the left of it

Input:
5 2 5 2
3 6 3 6
5 2 5 2
3 6 3 6

Output:
5 7 12 14 
8 16 24 32 
13 23 36 46 
16 32 48 64

'''
def integral_img(I):

    for row in range(len(I)):
        for col in range(len(I[0])): 
            # given pixel will be the sum of all pixels to the left and top of it, just need to take the previous sum left and up 
            if row == 0 and col == 0: # nothing to sum up for the top left 0,0 pixel
                pass
            else:
                if row - 1 >= 0 and col - 1 >=0:
                    I[row][col] = I[row][col] + I[row-1][col] + I[row][col-1] - I[row-1][col-1]  
                elif row - 1 >=0 and col - 1 < 0:    
                    I[row][col] = I[row][col] + I[row-1][col]
                elif col - 1 >=0 and row - 1 < 0:    
                    I[row][col] = I[row][col] + I[row][col-1]    
                
    return I


if __name__ == "__main__":
    # Example   
    I = [[5,2,5,2], [3, 6, 3, 6], [5, 2, 5, 2], [3, 6, 3, 6]  ]    

    I_int = integral_img(I)

    print(I_int)
