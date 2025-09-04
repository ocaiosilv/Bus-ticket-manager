class Produto:
    def __init__(self):
        # A chamada da função 'gera_preco()'
        # deve vir depois que a função foi definida.
        self.__preco = self.gera_preco()

    def gera_preco(self):
        # Esta função é chamada por __init__
        return 99.99

# Cria uma instância da classe Produto
meu_produto = Produto()
print(meu_produto.__preco)