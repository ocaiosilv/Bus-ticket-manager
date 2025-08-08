from onibus import Onibus



class Viagens:
    def __init__(self, id_viagem, origem, destino, data, hora, preco, tipoOnibus, assento):
        self.id_viagem = id_viagem
        self.origem = origem
        self.destino = destino
        self.data = data
        self.hora = hora
        self.preco = preco
        self.tipoOnibus = tipoOnibus
        self.assento = Onibus.get_assentos(tipoOnibus) ##retorna os assentos disponiveis ( uma lista de assentos )

    def get_id_viagem(self):
        return self.id_viagem

    def get_origem(self):
        return self.origem

    def get_destino(self):
        return self.destino

    def get_data(self):
        return self.data

    def get_hora(self):
        return self.hora

    def get_preco(self):
        return self.preco

    def get_tipoOnibus(self):
        return self.tipoOnibus

    def get_assento(self):
        return self.assento
    
    def set_id_viagem(self, id_viagem):
        self.id_viagem = id_viagem

    def set_origem(self, origem):
        self.origem = origem

    def set_destino(self, destino):
        self.destino = destino

    def set_data(self, data):
        self.data = data

    def set_hora(self, hora):
        self.hora = hora

    def set_preco(self, preco):
        self.preco = preco

    def set_tipoOnibus(self, tipoOnibus):
        self.tipoOnibus = tipoOnibus
        # Se trocar o tipo do ônibus, atualiza os assentos
        self.assento = Onibus.get_assentos(tipoOnibus)

    ##Usar pra debuggar até porque quando a gente tiver o Hud não vai precisar imprimir nada no print
    def imprime(self):
        print(f"ID: {self.id_viagem}")
        print(f"Origem: {self.origem}")
        print(f"Destino: {self.destino}")
        print(f"Data: {self.data}")
        print(f"Hora: {self.hora}")
        print(f"Preço: {self.preco}")
        print(f"Tipo de Ônibus: {self.tipoOnibus}")
        print(f"Assentos Disponíveis: {self.assento}")
        
    