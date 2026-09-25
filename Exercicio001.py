class Biscoito:
    def __init__(self):
        self.sabor = ""
        self.peso = 0.0
        self.assado = False
    def verificar_estado(self):
        if self.assado:
            return 'O biscoito está assado'
        else:
            return 'O biscoito está cru'


biscoito1 = Biscoito()
biscoito1.sabor = str(input('Digite o sabor do biscoito:'))
biscoito1.peso = float(input('Digite o peso de uma unidade de biscoito em gramas:'))
biscoito1.assado = str(input('O biscoito está assado? (Sim/Não):')).strip().lower()
if biscoito1.assado == 'sim':
    biscoito1.assado = True
else:
    biscoito1.assado = False

print(biscoito1.verificar_estado())

