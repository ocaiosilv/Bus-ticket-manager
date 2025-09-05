from onibus_convencional import OnibusConvencional
from onibus_executivo import OnibusExecutivo
from viagem import Viagem
from sistema_admin import SistemaAdmin
from sistema_vendas import SistemaVendas

onibus1 = OnibusConvencional("Zulaine","Honda",10,"Onibus sem problemas")
assentos = onibus1.get_assentos()
assento = assentos[4]

onibus1.set_assentos("B1","Giovani")
assento.imprime()

if onibus1.set_assentos("B2","augusto") == False:
    print("Lugar ocupado")
else:
    assentos[5].imprime()

viagem1 = Viagem(1,"Aracaju","Salvador","04/09/2025","7:00",120,onibus1)

sistema1 = SistemaAdmin()
sistema1.cadastrar_viagem("Aracaju","Salvador","Segunda","7:00",240,"Convencional","Zulaine","Honda")
