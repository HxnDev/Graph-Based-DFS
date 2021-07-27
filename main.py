###########################################################################################################################
#               Hassan Shahzad
#               18i-0441
#               CS-D
#               FAST-NUCES ISB
#               chhxnshah@gmail.com
###########################################################################################################################

################################################### Global Variables #####################################################
import abc                              # Used for abstract classes

import numpy as np
vertex=[]                               # Stores the neighbouring vertices
stack=[]                                # Will be used in DFS


################################################# Graph Class Declaration #################################################

class Graph(abc.ABC):                                          # Abstract Class

	def __init__(self, numVertices, directed=False):
		self.numVertices = numVertices                         # Number of vertices
		self.directed = directed                               # Is directed class or not

	@abc.abstractmethod
	def add_edge(self, v1, v2, weight):
		pass                                                   # We donot implement abstract method. The class importing will implement

	@abc.abstractmethod
	def get_adjacent_vertices(self, v):
		pass	

	@abc.abstractmethod
	def get_indegree(self, v):                                 # Number of vertices connected
		pass	

	@abc.abstractmethod
	def get_edge_weight(self, v1, v2):
		pass

	@abc.abstractmethod
	def display(self):	                                       # Displays graph
		pass

###########################################################################################################################

####################################################### Class Declaration #################################################
## Represents the graph as an adjacency matrix.

class AdjacencyMatrixGraph(Graph):                                                    # This class inherits "Graph" class


	def __init__(self, numVertices, directed=False):
		super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)             # Calling superclass to constructor

		self.matrix = np.zeros((numVertices, numVertices)) 

	def add_edge(self, v1, v2, weight=1):
		if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
			raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

		if weight < 1:
			raise ValueError("An edge cannot have weight < 1")	

		self.matrix[v1][v2] = weight
		if self.directed == False:
			self.matrix[v2][v1] = weight

	def get_adjacent_vertices(self, v):                                               # Returns connecrted vertices
		if v < 0 or v >= self.numVertices:
			raise ValueError("Cannot access vertex %d" % v)

		adjacent_vertices = []
		for i in range(self.numVertices):
			if self.matrix[v][i] > 0:
				adjacent_vertices.append(i)

		return adjacent_vertices		

	def get_indegree(self, v):
		if v < 0 or v >= self.numVertices:
			raise ValueError("Cannot access vertex %d" % v)

		indegree = 0
		for i in range(self.numVertices):
			if self.matrix[i][v] > 0:
				indegree = indegree + 1	
		
		return indegree	

	def get_edge_weight(self, v1, v2):
		return self.matrix[v1][v2]

	def display(self):
		for i in range(self.numVertices):
			for v in self.get_adjacent_vertices(i):
				print(i, "-->", v)

###########################################################################################################################
################################################ DFS Function Implemented #################################################

def DFS(graph, visited, goal, current=0):
    if (current==goal):                                         # Checks if current is the node we are searching for
        print("Current = ",current)
        print("Goal = ",goal)
        print("Solution Found!")
        return
    else:
        visited.append(current)                                 # Once the node is visited, its stored in the array
        vertex=g.get_adjacent_vertices(current)                 # Getting its neighbouring arrays
        i=0
        while i<len(vertex):
            if vertex[i] not in visited:
                stack.append(vertex[i])                         # Filling the stack
                current=vertex[i]                               # Current gets the next node
                if(current==goal):
                    print("Current = ",current)
                    print("Goal = ",goal)
                    print("Solution Found!")
                    return()
                else:
                    DFS(graph,visited,goal,current)             # Recursive call
            i=i+1

###########################################################################################################################

g = AdjacencyMatrixGraph(9)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 7)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(6, 3)
g.add_edge(3, 4)
g.add_edge(6, 8)

#for i in range(9):
#    print("Adjacent to: ", i, g.get_adjacent_vertices(i))

#for i in range(9):
#     print("Indegree: ", i, g.get_indegree(i))

#for i in range(9):
#    for j in g.get_adjacent_vertices(i):
#       print ("Edge weight: ", i, " ", j, " weight: ", g.get_edge_weight(i, j))


visited=[]

g.display()
DFS(g,visited,7,0)                            # Function being called

######################################################################################################################
################################################### THE END ##########################################################
######################################################################################################################
