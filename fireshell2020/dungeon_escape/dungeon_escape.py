from pwn import *
import sys 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        self.timers = [1 for row in range(vertices)]
  
    def printSolution(self, dist): 
        print "Vertex \tDistance from Source"
        for node in range(self.V): 
            print node, "\t", dist[node]

    def trueDistance(self,du,u,v):
        while du % self.timers[u] != 0:
            du = du + 1
        return du + self.graph[u][v]
              
    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 
  
        # Initilaize minimum distance for next node 
        min = sys.maxint 

        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
  
    # Funtion that implements Dijkstra's single source  
    # shortest path algorithm for a graph represented  
    # using adjacency matrix representation 
    def dijkstra(self, src, tgt): 
  
        dist = [sys.maxint] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 

            # Put the minimum distance vertex in the  
            # shotest path tree 
            sptSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > (self.trueDistance(dist[u],u,v)): 
                        dist[v] = self.trueDistance(dist[u],u,v) 
  
        #self.printSolution(dist)
        return dist[tgt]
  
# Test program 
g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]; 
  
g.dijkstra(0,8); 

g = Graph(5) 
g.graph = [
        [0,3,4,0,0],
        [3,0,0,2,12],
        [4,0,0,1,0],
        [0,2,1,0,4],
        [0,12,0,4,0],
        ]
g.timers = [1,4,3,7,1]
print(g.dijkstra(0,4))


def solve(first):
    p.recvuntil("Challenge")
    p.recvline()
    if first: 
        p.recvline()
    
    data = p.recvline().split()
    nodes = int(data[0])
    edges = int(data[1])
    print(nodes)   
    print(edges)   
    data = p.recvline().split()
    timers = [int(x) for x in data]
 
    g = Graph(nodes)
    g.timers = timers

    for i in range (0,edges):
        data = [int(x) for x in p.recvline().split()]
        g.graph[data[0]-1][data[1]-1] = data[2]
        g.graph[data[1]-1][data[0]-1] = data[2]

    data = [int(x) for x in p.recvline().split()]
    
    print(g.graph)
    answer = g.dijkstra(data[0]-1,data[1]-1)
    print(answer)
    p.sendline(str(answer))
    print(p.recv())

p = remote("142.93.113.55", 31085)
p.sendline("start")

solve(True)
for i in range(0,49):
    solve(False)

p.interactive()
p.close()
