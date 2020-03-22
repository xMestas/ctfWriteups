The solution to this problem is a modified version of dijkstra.  It is almost the same, just when you calculate the time to travel a path, you must also add waiting for the gate at the end.

I took a dijkstra solution from geekforgeek online: https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/

I modified their code to solve this problem, and then I used pwn tools to interface with the challenge and solve all the things.  Solve 50 levels, and it gives the flag.  It finishes with plenty of time to spare.  
