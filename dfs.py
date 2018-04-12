#######################################################################################################################################################################
# Description: An implementation of the SCC algorithm (Kosaraju's two-pass algorithm).
# File: dfs.py
#######################################################################################################################################################################

from pythonds.graphs import Graph, Vertex

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self, nodeOrd, sccs, scc):   
        # First pass, picks an arbitrary vertex to start DFS.
        if len(nodeOrd) == 0:

            # Sets vertex colors to white, meaning not explored.
            for aVertex in self:
                aVertex.setColor('white')
                aVertex.setPred(-1)
                
            # For every non explored vertex in the graph, call dfsvisit.
            for aVertex in self:
                if aVertex.getColor() == 'white':
                    self.dfsvisit(aVertex, nodeOrd, sccs, scc)
                    
        # Second pass, sequentially chooses vertices from nodeOrd.
        else:

            # Sets vertex colors to white, meaning not explored.
            for aVertex in self:
                aVertex.setColor('white')
                aVertex.setPred(-1) 
            for aVertex in nodeOrd:
                aVertex.setColor('white')
                aVertex.setPred(-1)
                
            # For every non explored vertex in nodeOrd, call dfsvisit.
            for aVertex in nodeOrd:
                if aVertex.getColor() == 'white':
                    # If a new non explored vertex needs to be fetched then add the scc to the list of sccs.
                    sccs.append(scc)
                    scc = []
                    self.dfsvisit(aVertex, nodeOrd, sccs, scc)

    def dfsvisit(self, startVertex, nodeOrd, sccs, scc):
        # Add the vertex to the scc if it's not already in there.
        if startVertex not in scc:
            scc.append(startVertex)
            
        # Set vertex color to gray, meaning it is being explored.
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)

        # Explore all vertices connected to startVertex.
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex, nodeOrd, sccs, scc)

        # Set vertex color to black, meaning it has been explored.
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

        # When the finish time has been set for a vertex, append the startVertex to nodeOrd.
        nodeOrd.append(startVertex)
        
