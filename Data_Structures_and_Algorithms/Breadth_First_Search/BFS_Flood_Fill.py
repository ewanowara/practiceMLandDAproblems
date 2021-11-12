'''
Flood Fill Problem: mark each connected component with a different number. 
It's a connected component if next to the non-zero pixel from up, down, left, or right

Input:

img = 
1 0 1 1 0
0 1 0 1 0 
1 1 1 1 1
0 0 1 0 1
1 0 0 0 0

(row,col) = 2,2 # start
p = 2

Output:
1 0 2 2 0
0 2 0 2 0 
2 2 2 2 2
0 0 2 0 2
1 0 0 0 0
'''

def flood_fill(img,row,col,p):
    # (row,col) - start pixel
    # p - new value to change the connected components into

    # find starting pixel value to see which pixels are connected to it
    start = img[row][col]
    # Q initialize queue
    Q = [(row,col)] # starting pixel 
    visited = set() 

    while len(Q) > 0: 
        row, col = Q.pop(0) # remove the first vertex from queue and grab those coordinates to add them to the visited set
        visited.add((row,col))
        img[row][col] = p # transform that pixel to the new value p
        
        for row, col in neighbors(img, row, col, start): 
            # print(row)
            # print(col)
            if (row, col) not in visited: 
                Q.append((row,col))
            # print(Q)    
    return img #transformed image             
                
def neighbors(img, row, col, start): # function to go through all neighbors of a pixel   
    indices = []
    # check if the pixel is valid and within the image bounds
    if row-1 >= 0 and img[row-1][col] == start: 
        indices.append((row-1,col))  
    if row+1 < len(img) and img[row+1][col] == start:     
        indices.append((row+1,col))  
    if col-1 >= 0 and img[row][col-1] == start:    
        indices.append((row,col-1))   
    if col+1 < len(img[0]) and img[row][col+1] == start:     
        indices.append((row,col+1))  
    return indices    

if __name__ == "__main__":
    # Example   
    img = [[1, 0, 1, 1, 0], [0, 1, 0, 1, 0], [1, 1, 1, 1, 1], [0, 0, 1, 0, 1], [1, 0, 0, 0, 0]]

    row = 2
    col = 2
    p = 2

    img_new = flood_fill(img,row,col,p)

    print(img_new)