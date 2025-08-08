class Onibus:
    def __init__(self, modelo, fabricante, numrodas, descricao, tipo_onibus):
        self.__modelo = modelo
        self.__fabricante = fabricante
        self.__numrodas = numrodas
        self.__descricao = descricao
        self.__tipo_onibus = tipo_onibus

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_fabricante(self):
        return self.__fabricante

    def set_fabricante(self, fabricante):
        self.__fabricante = fabricante

    def get_numrodas(self):
        return self.__numrodas

    def set_numrodas(self, numrodas):
        self.__numrodas = numrodas

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_tipo_onibus(self):
        return self.__tipo_onibus

    def set_tipo_onibus(self, tipo_onibus):
        self.__tipo_onibus = tipo_onibus

    def imprime(self):
        print("Modelo:", self.__modelo)
        print("Fabricante:", self.__fabricante)
        print("Número de rodas:", self.__numrodas)
        print("Descrição:", self.__descricao)
        print("Tipo de ônibus:", self.__tipo_onibus)

class OnibusExecutivo(Onibus):
    def __init__(self, modelo, fabricante, numrodas, descricao):
        super().__init__(modelo, fabricante, numrodas, descricao, "Executivo")
        self.__assentos_semi_leito = [0] * 48
        self.__assentos_leito = [0] * 12

    def get_assentos_semi_leito(self):
        return self.__assentos_semi_leito

    def set_assentos_semi_leito(self, qualAssento, tipoPassageiro):
        if tipoPassageiro == "Comum":
            self.__assentos_semi_leito[qualAssento] = 1
        else:
            self.__assentos_semi_leito[qualAssento] = 2

    def get_assentos_leito(self):
        return self.__assentos_leito

    def set_assentos_leito(self, lista):
        self.__assentos_leito = lista

    def imprime(self):
        super().imprime()
        print("Assentos Semi-Leito ainda livres: ", len(self.__assentos_semi_leito))
        print("Assentos Leito ainda livres: ", len(self.__assentos_leito))

class OnibusConvencional(Onibus):
    def __init__(self, modelo, fabricante, numrodas, descricao):
        super().__init__(modelo, fabricante, numrodas, descricao, "Convencional")
        self.__assentos = [0] * 48

    def get_assentos(self):
        return self.__assentos

    def set_assentos(self, lista):
        self.__assentos = lista

    def imprime(self):
        super().imprime()
        print("Assentos:", len(self.__assentos))

