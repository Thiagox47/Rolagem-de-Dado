from random import randint

escolha = str('')
while escolha != "N":
    print('-||-'*9)
    print("-ROLAGEM DE DADOS-")
    teste = int(input("Deseja rolar um dado de quantos lados?"))
    print("A sua rolagem deu: {}".format(randint(1,teste)))
    print('-||-'*9)
    escolha = str(input("Deseja continuar [S/N]:")).upper()
