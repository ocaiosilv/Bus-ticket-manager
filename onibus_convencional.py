from onibus import Onibus
from assento import Assento

class OnibusConvencional(Onibus):
    def __init__(self, modelo, fabricante, numrodas, descricao):
        super().__init__(modelo, fabricante, numrodas, descricao, "Convencional")
        # no git tava assim: self.assentos = self.gera_assentos()
        # aqui eu deixei privado (__assentos) pq é melhor encapsular
        self.__assentos = self.gera_assentos()

    def gera_assentos(self):
        # gera a lista na ordem "A1,A2,A3,A4,B1,B2,..." q nem vc fez mrm
        lista_assentos = []
        fileiras = "ABCDEFGHIJKL"
        
        for numero in range(1, 5): # mudei aqui porque tava tipo criando em linha reta, n tava ficando a gridzinha
            for letra in fileiras:
                numero_do_assento = f"{letra}{numero}"
                novo_assento = Assento(numero_do_assento, False)
                lista_assentos.append(novo_assento)
        return lista_assentos

    def get_assentos(self):
        return self.__assentos
    

    # tirei o converte assento, se foda, ai usei o get numero que tinha em assento, fica até melhor, que a gente usa mais função q nos criou

    def set_assentos(self, numero_assento, passageiro):
        for assento in self.__assentos:
            if assento.get_numero() == numero_assento and not assento.get_ocupado():
                assento.set_passageiro(passageiro)
                assento.set_ocupado(True)
                return True
        return False
        
    def imprime(self):
        super().imprime()
        livres = sum(1 for a in self.__assentos if not a.get_ocupado())
        print(f"Assentos: {len(self.__assentos)} (Livres: {livres})")