import os 
os.system

class Engenheiro:
    def __init__(self, nome, crea):
        self. nome = nome
        self. crea = crea 

        def exibir_detalhes(self):
            print(f"Engenheiro: {self.nome}")
            print(f"CREA: {self.crea}")

engenheiro1 = Engenheiro("João Silva", "123456-7")
engenheiro1.exibir_detalhes()