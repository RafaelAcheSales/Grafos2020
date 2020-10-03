class Grafo:
    def __init__(self, arquivo):
       self.ler(arquivo)

    def qtdVertices(self):
        return len(self._V)

    def qtdArestas(self):
        return len(self._E)

    def grau(self, vertice):
        grau = 0
        for aresta in self._E:
            if vertice in aresta:
                grau += 1
        return grau

    def rotulo(self, vertice):
        return self._V[vertice]
    
    def vizinhos(self, vertice):
        vizinhos = []
        for aresta in self._E:
            if vertice == aresta[0]:
                vizinhos.append(aresta[1])
            elif vertice == aresta[1]:
                vizinhos.append(aresta[0])
        return vizinhos

    def hasAresta(self, u, v):
        for aresta in self._E:
            if u in aresta and v in aresta:
                return True
        return False

    def peso(self, u, v):
        for aresta in self._E:
            if u in aresta and v in aresta:
                return aresta[2]
        return float("inf")


    def ler(self, arquivo):
        file = open(arquivo, 'r')
        n_vertices = file.readline().split(" ")[1]
        vertices = dict()
        arestas = []
        for x in range(int(n_vertices)):
            line = file.readline().split(" ")
            vertices[int(line[0])] = line[1].rstrip('\n')
        file.readline()
        line = file.readline()
        while line :
            line = line.split(" ")
            arestas.append((int(line[0]), int(line[1]), int(line[2])))
            line = file.readline()
        self._V = vertices
        self._E = arestas
        
if __name__ == "__main__":
    grafo = Grafo("grafos.txt")
    print(grafo.peso(4, 2))
    print(grafo.rotulo(2))
    print(grafo.vizinhos(2))
    print(grafo.grau(2))
    print(grafo.hasAresta(4, 2))