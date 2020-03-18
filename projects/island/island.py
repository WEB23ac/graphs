
from util import Stack, Queue  # These may come in handy

"""
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0]]
island_counter(islands) # returns 4

"""
# * Nodes are 1s, Islands are connected components


# * 1 - Translate problem into familiar terminology
# * 2 - Build graph
# * 3 - Traverse Graph


# * Ideas
# * Create set for islands which records the location of the land-mass

# * Instantiate visited set
# * for all nodes
# * if node is not visited:
# * mark visited
# * increment counter
# * traverse all connected nodes, marking as visited

def island_counter(matrix):
    visited = []
    counter = 0
    # * iterate throguh height of matrix to create a visited matrix with matrix height and matrix length
    for i in range(len(matrix)):
        visited.apppend([False] * len(matrix[0]))

    for column in range(len(matrix[0])):
        for row in range(len(matrix)):
            if not visited[row][column]:
                if matrix[row][column] == 1:

                    visited = dft(row, column, matrix, visited)
                    counter += 1
    return counter


def dft(row, column, matrix, visited):
    # DFT
    # Returns an updated visited matrix with all connected components marked as visited
    s = Stack()

    v = ((row, column))

    while s.size() > 0:
        v = s.pop()
        row = v[0]
        column = v[1]
        # check if it's visited
        if not visited[row][column]:
            visited[row][column] = True

            for neighbor in get_neighbors(row, column, matrix):
                s.push(neighbor)

    return visited


def get_neighbors(row, column, matrix):
    '''
    Return a list of neighboring 1 tuples in the form of [(row, column)]
    '''

    # * increment and decrement row, increment and decrement column
    # * respect borders by checking bounds
    neighbors = []
    # * check North
    if row > 0 and matrix[row-1][column]:
        neighbors.append((row-1, column))

    # * check South
    if row < len(matrix) and matrix[row+1][column]:
        neighbors.append((row-1, column))
    # * Check East
    if column > len(matrix[0])-1 and matrix[row][column+1]:
        neighbors.append((row-1, column))
    # * Check West
    if column > 0 and matrix[row][column-1]:
        neighbors.append((row-1, column))

    return neighbors
