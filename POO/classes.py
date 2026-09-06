class Canal:
    def __init__(self,nome,descricao,inscritos):
        self.nome=nome
        self.descricao=descricao
        self.inscritos=inscritos
    def inscrever(self,quantidade=1):
        self.inscritos+=quantidade

canal_nathan=Canal("nathan","opa salve",12)

canal_jose=Canal("josezin GAYMER","ai pai para",10000000)

print(f"inscritos atual do nathan: {canal_nathan.inscritos}")
canal_nathan.inscrever()
print(f"inscritos atual do nathan: {canal_nathan.inscritos}")
