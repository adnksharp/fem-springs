from numpy import array, multiply, delete
from numpy.linalg import solve

class fem():
    U = array([])
    K = array([])
    R = array([])
    
    def __init__(self):
        pass
    
    def calculate(self, n, nodes, forces, findex, k, bc):
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
            U[local[i]] = SU[i]
        U = array(U)
        R = K.dot(U)
        self.K = K
        self.R = R
        self.U = U
    
    def getK(self):
        out = ['\t'.join(map(str, k))for k in self.K]
        return '\n'.join(out)
    
    def getR(self):
        return '\n'.join(str(R) for R in self.R)
    
    def getU(self):
        return '\n'.join(str(U) for U in self.U)