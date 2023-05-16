class ElementoFila():

    def __init__(self, valor, proximo):
        self.valor = valor
        self.proximo = proximo

class Fila():

    def __init__(self):
        self.ultimo = None
        self.primeiro = None
        self.qtd = 0
def main():
    f = fila()
    print(f)

if __name__ == "__main__":
    main()
    