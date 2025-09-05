from onibus import Onibus

class Viagem:
    def __init__(self, id_viagem, origem, destino, dias_da_semana, hora, preco, onibus: Onibus):
        self.__id_viagem = id_viagem
        self.__origem = origem
        self.__destino = destino
        self.__dias_da_semana = dias_da_semana
        self.__hora = hora
        self.__preco = preco
        self.__onibus = onibus

    def get_id_viagem(self):
        return self.__id_viagem

    def set_id_viagem(self, id_viagem):
        self.__id_viagem = id_viagem

    def get_origem(self):
        return self.__origem

    def set_origem(self, origem):
        self.__origem = origem

    def get_destino(self):
        return self.__destino

    def set_destino(self, destino):
        self.__destino = destino

    def get_dias_da_semana(self):
        return self.__dias_da_semana

    def set_dias_da_semana(self, dias):
        self.__dias_da_semana = dias

    def get_hora(self):
        return self.__hora

    def set_hora(self, hora):
        self.__hora = hora

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

    def get_onibus(self):
        return self.__onibus

    def set_onibus(self, onibus: Onibus):
        self.__onibus = onibus

    def imprime(self):
        print(f"ID: {self.__id_viagem}")
        print(f"Origem: {self.__origem}")
        print(f"Destino: {self.__destino}")
        print(f"Dias da semana: {self.__dias_da_semana}")
        print(f"Hora: {self.__hora}")
        print(f"Preço: {self.__preco}")
        print(f"Tipo de ônibus: {self.__onibus.get_tipo_onibus()}")
        print(f"Assentos disponíveis:", {self.__onibus.get_assentos()})
