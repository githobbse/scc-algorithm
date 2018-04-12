####################################################################################
# Description: An implementation of the SCC algorithm (Kosaraju's two-pass algorithm).
# File: README.txt
####################################################################################

The file scc.py is an implementation of the Kosaraju's two-pass algorithm. This program takes a file as input from the command line. A graph (g) and its reverse (gR) are then built from the list of edges in the input file.

DFS is then called on gR in order to determine the reverse postorder of g. The order in which nodes are searched in this first pass through DFS does not matter. DFS is then called on g, following the order of the nodes in the reverse postorder previously determined. This second pass is performed in order to determine the SCCs in the graph, and their sizes. Every time a node's color is set to black (indicating that it has been fully explored), the node is added to an SCC. All components of an SCC have been found when a new node (not connected to any nodes already in the SCC) must be fetched.

After all SCCs have been determined, the program simples sorts their sizes in descending order, and prints the results out to the command line.