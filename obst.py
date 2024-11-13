# implement program to build obst using dp
# time complexity: O(n^3)
# space complexity: O(n^2)

def obst(p, q, n):
    c = [[0] * (n+1) for _ in range(n+2)]
    w = [[0] * (n+1) for _ in range(n+2)]
    r = [[0] * (n+1) for _ in range(n+2)]

    