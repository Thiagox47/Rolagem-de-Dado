import random
import playsound

teste = int(input("Deseja rolar um dado de quantos lados?"))
playsound.playsound("diceroll.mp3")
print("A sua rolagem deu: {}".format(random.randint(1,teste)))
