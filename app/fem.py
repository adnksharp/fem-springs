from numpy import array, multiply

def calculate(elements, n, nodes, forces, findex, k):
    K = [[0 for i in range(n)] for i in range(n)]
    K = array(K)
    for i in range(len(k)):
        klocal = multiply(array([[1, -1], [-1, 1]]), k[i])
        for j in range(2):
            for l in range(2):
                K[nodes[i][j]][nodes[i][l]] += klocal[j][l]
    print(K)