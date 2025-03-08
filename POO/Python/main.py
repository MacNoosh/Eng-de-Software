#Gasta mais memória
#import Carro as Car 

#Gasta menos memíria
from Carro import Carro as Car

#carro1 = Car

carro1 = Car("Fiat", "Uno com escada", 2009, "branco", "XTS1049")

carro2 = Car("VW","Fusca",1959,"Amarelo","LOR1049")

#print(carro1, "\n", carro2)

#usando cadastro de vendas
#carro3 = Car.cadastro_venda()

print(carro1, "\n", carro2)

carro2.ligar_carro()

carro2.running()

for i in range(4):
    carro2.running()

for i in range(6):
    carro2.freiar()
