## Definindo metodo construtor da classe
class Carro:
    def __init__(self,marca,modelo, ano, cor, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.placa = placa
        self.is_running =  False
        self.velocidade = 0

    #método de apresentação  
    #método de classe                       
    def __str__(self):
        return f"""
O carro de Marca {self.marca} e Modelo {self.modelo}
do Ano {self.ano} e Cor {self.cor} saiu da loja e 
foi emplacado, a placa é {self.placa}
        """    

#método de instância 
    @classmethod
    def cadastro_venda(cls):
        marca = input ("Digite a marca do carro comprado: ")
        modelo = input ("Digite o modelo do carro comprado: ") 
        ano =  int (input("Digite aqui o ano do carro comprado: "))        
        cor = input ("Digite a cor do carro comprado: ")
        placa = input("Digite a placa do carrop comprado: ")
        return cls(marca, modelo, ano, cor, placa)
    
    def ligar_carro(self):
        if not self.is_running:
            self.is_running = True
            print("O carro foi ligado........RUM RUM RUM")
        else:
            print("O carro já esta ligado")

    def running(self):
        if self.is_running:
            self.velocidade += 5
            print(f"A velocidade do carro é {self.velocidade}Km/h")
        else:
            print(f"O carro {self.modelo} esta desligado, ligue o carro primeiro")
    
    def freiar(self):
        if self.is_running and self.velocidade> 0:
            self.velocidade -= 5
            print(f"A velocidade do carro é {self.velocidade}Km/h")
        else:
            print(f"O carro {self.modelo} esta desligado ou sua velocidade já é 0Km/h, ligue o carro primeiro")

# montar um acelerador qui irá acelerar com base na marcha definida(acrescer a marcha de acordo com a velocidade), 
# para marcha ré ele tem que estar com base na velocidade entre 0 e 1
    
