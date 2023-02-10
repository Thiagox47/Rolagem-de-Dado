import sqlite3
from time import sleep
from random import randint

def verificar_usuario(username):
    # Conectar ao banco de dados
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    
    # Verificar se o usuário já existe no banco de dados
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    
    # Fechar conexão com o banco de dados
    connection.close()
    
    # Se o usuário for encontrado, retornar True
    if result:
        return True
    else:
        return False

def register_user():
    username = input('Insira seu nome de usuário: ')
    password = input('Insira sua senha: ') 
    if verificar_usuario(username) == True:
        print("Usuario já existe tente outro!")
    else:
        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', (username, password))
        connection.commit()
        connection.close()
        print('Usuário registrado com sucesso!')
    sleep(2)
    main()

def login_user():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    username = input('Insira seu nome de usuário: ')
    password = input('Insira sua senha: ')
    cursor.execute('''SELECT * FROM users WHERE username = ? AND password = ?''', (username, password))
    result = cursor.fetchone()
    if result:
        print('Login efetuado com sucesso!')
        diceroll()
    else:
        sleep(1)
        print('Nome de usuário ou senha inválidos. Por favor, tente novamente.')
        sleep(1)
        main()
    connection.close()

def diceroll():
    print("Bem vindo a rolagem e dado secreta!")
    sleep(1)
    print("Será que você está com sorte hoje?")
    sleep(1)
    yesorno = "s"
    while yesorno == 's':
        dice = int(input("Deseja rolar um dado de quantos lados? "))
        roll = randint(1,dice)
        print("Rolando os dados...")
        sleep(1)
        print("Sua rolagem deu: {}".format(roll))
        sleep(1)
        if roll >= (dice / 2) + 1:
            print("CARAMBA QUE SORTE A SUA EM!")
            sleep(1)
            yesorno = input("Você deseja continuar rolando dados?[S/N]: ").lower().strip()
            while yesorno != "s" and yesorno != "n":
                sleep(1)
                print("Entrada inválida. Por favor, digite S ou N.")
                sleep(1)
                yesorno = input("Você deseja continuar rolando dados?[S/N]: ").lower().strip()
        else:
            print("Você não está com muita sorte hoje! Tente novamente!")
            yesorno = str(input("Você deseja continuar rolando dados?[S/N]: ").lower().strip())
            while yesorno != "s" and yesorno != "n":
                sleep(1)
                print("Entrada inválida. Por favor, digite S ou N.")
                sleep(1)
                yesorno = input("Você deseja continuar rolando dados?[S/N]: ").lower().strip()
        print("Até mais!")

def main():
    print('1. Entrar\n2. Registrar\n')
    option = int(input('Escolha uma opção: '))
    if option == 1:
        login_user()
    elif option == 2:
        register_user()
    else:
        print('Opção inválida. Por favor, tente novamente.')

if __name__ == '__main__':
    main()
