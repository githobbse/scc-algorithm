#######################################################################################################################################################################
# Description: An implementation of the SCC algorithm (Kosaraju's two-pass algorithm).
# File: scc.py
#######################################################################################################################################################################

import sys
from pythonds.basic import Stack
from pythonds.graphs import Graph, Vertex
from dfs import DFSGraph

def main():
    g = DFSGraph()
    gR = DFSGraph()
    nodeOrd = []
    sccs = []
    scc = []
    s = Stack()

    # Inputs testFile from command line and builds graph g and the reversed graph gR.
    testFile = open(sys.argv[1], 'r')
    for edge in testFile:
        head = edge.split()[0]
        tail = edge.split()[1]
        g.addEdge(head, tail)
        gR.addEdge(tail, head)

    # First pass - builds nodeOrd, the reverse postorder of g.
    DFSGraph.dfs(gR, nodeOrd, sccs, scc)

    # Second pass - builds a list of all SCCs.
    DFSGraph.dfs(g, nodeOrd, sccs, scc)

    # Prints first 10 SCC sizes.
    sccSizes = []
    for scc in sccs:
        sccSizes.append(len(scc))
    sortedSizes = sorted(sccSizes, reverse=True)[:10]
    for i in sortedSizes:
        sys.stdout.write(str(i) + ',')

main()
