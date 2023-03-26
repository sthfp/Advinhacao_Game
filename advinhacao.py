import random

def jogar():
    print("********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    print(numero_secreto)
    rodada = 1
    pontos = 1000
    print("Qual nível de dificuldade você gostaria de jogar?")
    print("(1) Fácil (2) Médio (3) Difícil")
    dificuldade = int(input("Informe qual nível desejado: "))


    if(dificuldade == 1):
        total_de_tentativas = 20
    elif(dificuldade == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1,total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if(chute<1 or chute>100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute >  numero_secreto
        menor = chute <    numero_secreto

        if(acertou):
            print("Você acertou!")
            print("Sua pontuação foi {}".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! Seu chute foi maior do que o número secreto")
            elif(menor):
                print("Você errou! Seu chute foi menor do que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("Fim do jogo")
if(__name__ == "__main__"):
    jogar()