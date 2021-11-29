# We are initializing the number of vertices in our graph
no_vertices = 7

# create an array that will be used in tracking the vertex
selected_vertex = [0, 0, 0, 0, 0, 0, 0]

# the first vertex is set to true so that it could be the beginning vertex
selected_vertex[0] = True


# printing for edge and weight
print("This are the Edges : With their Weights\n")

# function
def prims(Graph):
    
    # defining an infinite integer that will act as a placeholder 
    INF = float("inf")

    # we are setting the number of edges to zero
    no_edge = 0
    r_index = 0
    c_index= 0
    
    #  while loop checking the condition that the edges in the minimum spanning tree are less than the number of vertices subtracted by one
    while (no_edge < no_vertices- 1): 
        
        min = INF
        
        for p in range(no_vertices):
            
            # check if the selected vertex is already in the set
            if selected_vertex[p]:
                
                for q in range(no_vertices):
                    
                    # shows not selectecd and the existense of an edge
                    if ((not selected_vertex[q]) and Graph[p][q]):  
                        
                        # commparrisons to make sure that the minimum is sleceted
                        if min > Graph[p][q]:
                            min = Graph[p][q]
                            r_index= p
                            c_index= q
                            
        print(str(r_index) + "-->" + str(c_index) + ":" + str(Graph[r_index][c_index]))
        
        # reseting the vertex that we found the minimum cost of the edge to true
        selected_vertex[c_index] = True
        
        # increment the number of edges by one
        no_edge += 1
        
Graph = [[0, 28, 0, 0, 0, 10, 0],
    [28, 0, 16, 0, 0, 0, 14],
    [0, 16, 0, 12, 0, 0, 0],
    [0, 0, 12, 0, 22,0, 18],
    [0, 0, 0, 22, 0, 25, 24],
    [10, 0, 0, 0, 25, 0, 0],
    [0, 14, 0, 18, 24, 0, 0],
    ]
prims(Graph)