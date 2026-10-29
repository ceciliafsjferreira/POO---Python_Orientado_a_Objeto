from rich import print as rprint
from rich import inspect

class ContaBancária:
    """Classe que representa uma conta bancária com saldo e operações."""

    def __init__(self, id, nome , saldo = 0.0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str__(self) :
        print(f'A conta bancária {self.id} de {self.titular} tem saldo de R$ {self.saldo:,.2f}')
 
    def deposito(self,valor):
        self.saldo += valor
        print(f'Depósito de R$ {valor:,.2f} realizado com sucesso!')

    def saque(self,valor):
        if valor > self.saldo:
            print( f'Saldo insuficiente para saque de R$ {valor:,.2f}.')
        else:    
            self.saldo -= valor
            print(f'Saque de R$ {valor:,.2f} realizado com sucesso!')  

c = ContaBancária(1123, "Cecília", 1000.00)
inspect(c)