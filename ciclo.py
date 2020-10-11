from grafo import Grafo
class Ciclo:
    def __init__(self, file):
        self.g = Grafo(file)
        self.C = dict()

    def buscar_subciclo(self, v):
        Ciclo = []
        Ciclo.append(v)
        t = v
        while True:
            print(v, self.g.vizinhos(v))
            for vizinho in self.g.vizinhos(v):
                print(v, vizinho)  
                if not self.C[(v, vizinho)]:
                    self.C[(v, vizinho)] = True
                    self.C[(vizinho, v)] = True
                    Ciclo.append(vizinho)
                    v = vizinho
                    print("Coloquei V", v)
                    break
            if t == v:
                if len(Ciclo) == 1:
                    return (False, None)
                break

    def calcular_ciclo(self):
        for e in self.g.E:
            self.C[(e[0], e[1])] = False
            self.C[(e[1], e[0])] = False
        self.buscar_subciclo(3)

c = Ciclo("grafos.txt")
c.calcular_ciclo()
