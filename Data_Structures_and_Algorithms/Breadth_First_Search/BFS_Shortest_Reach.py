'''
Find Shortest Reach in a Graph: given the number of nodes, edges, and the adjacency list. 

n - number of nodes / vertices
m - number of edges
edges - array with edges from u to v: (u,v) (ADJACENCY LIST)
s - start

Input:
(4,2,(1,2),(1,3),1)

weight for each edge: +6
if no edge between a node and start: -1 

Output:

[6, 6, -1]

'''

def shortest_reach(n, m, edges, s):
    Q = [s] # initialize the queue with a starting node
    visited = set() # keep track of nodes which have already been visited
    level_list = [] # checks if a node was already at a given neighbor level
    level_list.append(s)
    level = 0 # which neighbor level we are on - use it to multiply the edge - distance from source node
    distance_array = [-1] * (n) # want it to be lenght n-1
    edge_weight = 6
    while len(Q) > 0: # while the queue is non-empty
        node = Q.pop(0) # access the first node in the queue   
        visited.add(node) # mark the node as visited
        neighbors = neighbor_fct(node, edges) # access all neighbors of node 

        for nn in neighbors:
            if nn not in level_list:
                print(str(nn) + ' not in level')
                level = level+1 
                level_list.extend(neighbors) # so that we don't keep increasing levels for the neighbors of the same node
            if nn not in visited: # check if the neighbor has been visited 
                Q.append(nn) # add to queue
                distance_array[nn-1] = edge_weight*level            
    # remove the index corresponding to the start node
    distance_array.pop(s-1)
    return distance_array               
    
def neighbor_fct(node, edges):
    neighbors = []
    # a neighbor of a given node is defined as the other element in the edge array
    for edge in edges:
        if edge[0] == node:
            neighbors.append(edge[1])
        elif edge[1] == node:
            neighbors.append(edge[0])        
    return neighbors   

if __name__ == "__main__":
    # Example  
    weight_list = shortest_reach(5, 3, [[1,2], [1,3], [3,4]], 3) #(4, 2, [[1,2], [1,3]], 1)
    print(weight_list)
