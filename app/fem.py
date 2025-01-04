from numpy import array, multiply, delete
from numpy.linalg import solve

def calculate(elements, n, nodes, forces, findex, k, bc):
    R = array([0 for i in range(n)])
    U = [0 for i in range(n)]
    local = [i for i in range(n)]
    for i in range(len(findex)):
        R[findex[i] - 1] = forces[i]
    K = array([[0 for i in range(n)] for i in range(n)])
    for i in range(len(k)):
        klocal = multiply(array([[1, -1], [-1, 1]]), k[i])
        for j in range(2):
            for l in range(2):
                K[nodes[i][j]][nodes[i][l]] += klocal[j][l]
    bc = array(bc)
    SK = delete(K, bc, axis=0)
    SK = delete(SK, bc, axis=1)
    SR = delete(R, bc)
    local = delete(local, bc).tolist()
    
    SU = solve(SK, SR).tolist()
    for i in range(len(local)):
        print(i, U[i], local[i], SU[i], U[local[i]], end='\t')
        U[local[i]] = SU[i]
        print(U[local[i]])
    U = array(U)
    R = K.dot(U)
    print(K, U, R)