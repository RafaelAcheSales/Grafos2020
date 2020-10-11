from grafo import Grafo
class Search:
    def __init__(self, file):
        self.g = Grafo(file)
        self.C = []
        self.A = []
        self.D = []

    def print_verticies(self, D):
        output = []
            
    def busca_em_largura(self, index):
        for vertice in range(self.g.qtdVertices()):
            self.C.append(False)
            self.D.append(float("inf"))
            self.A.append(None)
        self.C[index] = True
        self.D[index] = 0
        self.Q = []
        self.Q.append(index)
        while len(self.Q) > 0:
            u = self.Q.pop()
            for vizinho in g.vizinhos(u):
                if not self.C[vizinho]:
                    self.C[vizinho] = True
                    self.D[vizinho] = self.D[u] + 1
                    self.A[vizinho] = u
                    self.Q.append(vizinho)
        return self.D, self.A
