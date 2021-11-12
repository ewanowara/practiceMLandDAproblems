'''
Given a binary image, output the number of connected components defined as pixels = 1 with neighbors = 1 to the top, bottom, left and right 

Input:
1 1 0 0 0
1 1 0 1 0
1 1 0 0 0
0 0 0 1 1

Output:
3

'''

def mark_cell(X, row1, col1, num_rows, num_cols):
    # check boundaries
    if row1 < 0 or row1 >= num_rows or col1 < 0 or col1 >= num_cols:
        return X
    else:    
        if X[row1][col1] == 1: # not seen yet
            X[row1][col1] = 2
            # check neigbors in a recursive call
            if row1-1 >=0:
                X = mark_cell(X, row1-1, col1, num_rows, num_cols) 
            if row1+1 < num_rows:
                X = mark_cell(X, row1+1, col1, num_rows, num_cols) 
            if col1-1 >=0:    
                X = mark_cell(X, row1, col1-1, num_rows, num_cols) 
            if col1+1 <= num_cols: 
                X = mark_cell(X, row1, col1+1, num_rows, num_cols) 
    return X

def connected_components(X):    
    num_components = 0
    # check boundaries
    num_rows = len(X) 
    num_cols = len(X[0]) 

    if num_rows <= 0 and num_cols <= 0:
        return num_components
    else:     
        for row in range(num_rows):
            for col in range(num_cols):
                if X[row][col] == 1:
                    X = mark_cell(X, row, col, num_rows, num_cols) 
                    num_components = num_components + 1 
    return num_components



if __name__ == "__main__":
    # Example   
    Xt = [[1, 1, 0, 0, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1]]

    # Xt = [[1, 1, 0, 0 ], 
    #     [1, 0, 0, 0],
    #     [0, 0, 1, 1]]

    # Xt=[[1, 1, 0, 0,1],
    #    [1, 1, 0, 1, 1],
    #    [1, 1, 0, 0, 1],
    #    [0, 1, 1, 0, 1]]


    # Xt = [[0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0]]


    # Xt = [[1]]
    cell_out = connected_components(Xt)
    print(cell_out)