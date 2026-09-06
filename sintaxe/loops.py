cont=10
while cont>=1:
    print(cont)
    cont-=1

compras=["arroz","feijao","leite"]
for item in compras:
    print(f"vc precisa comprar : { item}")

numeros =[3,3,3,2,2,12,32,3,2,1,1,23]
for numero in numeros:
    if numero%2==0:
        print(numero)