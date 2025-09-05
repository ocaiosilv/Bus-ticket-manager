from onibus import Onibus
from assento import Assento

class OnibusConvencional(Onibus):
    def __init__(self, modelo, fabricante, numrodas, descricao):
        super().__init__(modelo, fabricante, numrodas, descricao, "Convencional")
        self.__assentos = self.gera_assentos()

    def gera_assentos(self):
        lista_assentos = []
        fileiras = "ABCDEFGHIJKL"
        
        for letra in fileiras:
            for numero in range(1,5):
                numero_do_assento = f"{letra}{numero}"
                novo_assento = Assento(numero_do_assento,False)
                lista_assentos.append(novo_assento)
                
        return lista_assentos


    def get_assentos(self):
        return self.__assentos
    
    def __converte_numero_do_assento(self,numero_assento):
        # Fazer raise para conferir se o número do assento é compatível
        letra = numero_assento[0]
        indice_letra = ord(letra) - ord('A')
        numero = int(numero_assento[1])
        indice = (indice_letra * 4) + (numero - 1)
        return indice

        

    def set_assentos(self, numero, passageiro):
        #Fazer raise de Passageiro
        numero_convertido = self.__converte_numero_do_assento(numero)
        if self.__assentos[numero_convertido].get_ocupado() == False:
            self.__assentos[numero_convertido].set_passageiro(passageiro)
            self.__assentos[numero_convertido].set_ocupado(True)
            return True
        return False
        
    def imprime(self):
        super().imprime()
        print("Assentos:", len(self.__assentos))