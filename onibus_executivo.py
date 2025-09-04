from onibus import Onibus

class OnibusExecutivo(Onibus):
    def __init__(self, modelo, fabricante, numrodas, descricao):
        super().__init__(modelo, fabricante, numrodas, descricao, "Executivo")
        self.__assentos_semi_leito = [[0]*12,[0]*12,[0]*12,[0]*12]
        self.__assentos_leito = [[0]*4,[0]*4,[0]*4]
       
    def get_assentos(self):
        assentos = {
            "Semi-Leito": self.__assentos_semi_leito,
            "Leito": self.__assentos_leito
        }
        return assentos
    
    def get_assentos_semileito(self):
        return self.__assentos_semi_leito

    def set_assentos_semi_leito(self, qualAssento, tipoPassageiro):
        if tipoPassageiro == "Comum":
            self.__assentos_semi_leito[qualAssento] = 1 # 1 representa que o assento está ocupado por um passageiro comum
        else:
            self.__assentos_semi_leito[qualAssento] = 2 # 2 representa que o assento está ocupado por um passageiro leito

    def get_assentos_leito(self):
        return self.__assentos_leito

    def set_assentos_leito(self, tipo, linha, coluna, passageiro):
        if tipo == "Semi-Leito":
            if 0 <= linha < len(self.__assentos_semi_leito) and 0 <= coluna < len(self.__assentos_semi_leito[0]):
                if self.__assentos_semi_leito[linha][coluna] == 0:
                    self.__assentos_semi_leito[linha][coluna] = passageiro 
                    return True
        elif tipo == "Leito":
            if 0 <= linha < len(self.__assentos_leito) and 0 <= coluna < len(self.__assentos_leito[0]):
                if self.__assentos_leito[linha][coluna] == 0:
                    self.__assentos_leito[linha][coluna] = passageiro
                    return True
        return False
    
    def assentos_livres(self, assentosTotais):
        total = []
        for numLinha, linha in enumerate(assentosTotais):
            for numColuna, coluna in enumerate(linha):
                if coluna == 0:
                    total.append([numLinha, numColuna])
        return total
    
    def imprime(self):
        super().imprime()
        print("Assentos Semi-Leito ainda livres: ", OnibusExecutivo.assentos_livres(self.__assentos_semi_leito))
        print("Assentos Leito ainda livres: ", OnibusExecutivo.assentos_livres(self.__assentos_leito))
