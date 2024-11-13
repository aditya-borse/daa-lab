# graph coloring using backtracking
# time complexity: O(m^n) [m is no. of colors and n is no. of vertices]
# space complexity: O(n)

def solveGraphColoring(graph, m):
    n = len(graph)
    color = [-1]*n

    def is_safe(v, c):
        for i in range(n):
            if graph[v][i] == 1 and color[i] == c:
                return False
    
        return True
    
    def backtrack(v):
        if v == n:
            return True
        
        for c in range(1, m+1):
            if is_safe(v, c):
                color[v] = c

                if backtrack(v+1):
                    return True
                
                color[v] = -1

        return False
    
    if backtrack(0):
        print("Assigned colors are: ")
        for i in range(n):
            print(f'Vertex {i+1} -> Color {color[i]}') 
    else:
        print("No solution exist")

if __name__ == '__main__':
    graph = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0]
    ] 
    m = 3  
    solveGraphColoring(graph, m)