
#nesse dicionário eu armazeno as configurações das jogadas para depois serem usadas com chamadas de funções
jogadas = {

    "JOGADA_1": 0,
    "JOGADA_2": 0,
    "SIMBOLO_JOGADA_1": "X",
    "SIMBOLO_JOGADA_2": "O"


}

#essa função é responsável por configurar o jogo
def iniciar_config(vez_jogador, vez_bot):

    mensagem_de_config = '''

    Esse jogo pode ser jogado usando bots (um programa que simula um jogador humano).

    A seguir você vai configurar o jogo


    '''

    #variáveis que controlam como o jogo seerá configurado // usei como uma lista pois posso assim passar os valores por referência

    quantidade_de_bots = [0] #quantos bots terão na partida
    bot_presente = [False] #se o jogo vai ter algum bot durante a partida
    jogada_de_inicio = ["X"] #qual marcação o primeiro jogador a jogar vai usar
    jogada_inimiga = ["O"] #qual marcação o jogador inimigo vai usar
    jogador_comeca = [True] #se o jogador humano vai começãr jogando ou não

    #aqui eu inicializo 2 variáveis que recebem as funções do jogo principal (posteriormente serão chamadas)
    JOGADOR = vez_jogador
    BOT = vez_bot

    #essa função é resposável por imprimir as configurações do jogo
    def exibir_config(quantidade_de_bots, bot_presente, jogada_de_inicio, jogador_comeca):
        print("Quantidade de bots : ", quantidade_de_bots[0], "\n")
        print("Bot presentes no jogo : ", bot_presente[0], "\n")
        print("Jogador inicia jogando : ", jogador_comeca[0], "\n")
        print("Inicia jogando como : ", jogada_de_inicio[0], "\n")


    ##essa de fato configura o jogo por meio das entradas do jogador
    #são 3 etapas: se o jogo tem bots ou não -> 
    # se tiver quantos vai ser -> 
    # se tiver bots e só for 1, quer começar jogando ou não (essa pergunta só faz sentido com bots, pois JOGADOR vs JOGADOR os próprios jogadores humanos decidem)
    def definir_config(quantidade_de_bots, bot_presente, jogada_de_inicio, jogador_comeca):
        while True:

            while True:   
                resposta = input("Quer bots no jogo (S ou N - caso tenha 2 jogadores humanos selecione N, caso seja um jogador sozinho selecione S)? : ").upper()

                if resposta == "S":
                    bot_presente[0] = True
                    break

                elif resposta == "N":
                    bot_presente[0] = False
                    break

                else:
                    print("\nResposta inválida, tente novamente com S ou N\n")

            print("\n\n\n")


            if bot_presente[0] == True:
                while True:
                    try:
                        if bot_presente[0] == True:
                            quantidade_de_bots[0] = int(input("Quantos bots você quer no jogo (1 ou 2 - 2 bots vai fazer com que um bot jogue contra o outro, você apenas poderá assistir) : "))
                            

                            if quantidade_de_bots[0] != 1 and quantidade_de_bots[0] != 2:
                                quantidade_de_bots[0] = 0
                                raise ValueError

                            else:
                                if quantidade_de_bots[0] == 2: jogador_comeca[0] = False 
                                break

                    except:
                        print("\nVocê não digitou um inteiro válido! Tente apenas 1 ou 2.\n")

            print("\n\n\n")


            if bot_presente[0] == True and quantidade_de_bots[0] == 1:
                while True:
                    jogador_comeca[0] = input("Deseja começar jogando (S ou N)? : ").upper()

                    if jogador_comeca[0] == "S":
                        jogador_comeca[0] = True
                        break

                    elif jogador_comeca[0] == "N":
                        jogador_comeca[0] = False
                        break

                    else:
                        print("\nResposta inválida, tente novamente com S ou N\n")


            print("\n\n\n")

            '''
            if jogador_comeca[0] == True:
                while True:
                    try:
                        jogada_de_inicio[0] = input("Você quer começar como \'X\' ou \'O\' (pode ser usado essas letras como resposta)? : ").upper()

                        if jogada_de_inicio[0] != "X" and jogada_de_inicio[0] != "O":
                            jogada_de_inicio[0] = "X"
                            raise Exception

                        else:
                            
                            break

                    except Exception:
                        print("\nVocê não digitou uma jogada inicial válida\n")
                    
            print("\n\n\n")'''
            

            exibir_config(quantidade_de_bots, bot_presente, jogada_de_inicio, jogador_comeca) #imprimo as configurações depois de serem feitas

            print("\n\n\n")

            #antes de sair do loop pergunto para o usuário se deseja continuar
            resposta = input("Deseja continuar (S - continua / qualquer entrada - permite reconfigurar o jogo) : ").upper()

            if resposta == "S":
                break

    #aqui a partida é contruída no dicionário do módulo (jogadas)
    def gerar_jogo(quantidade_de_bots, bot_presente, jogada_de_inicio, jogador_comeca, jogada_inimiga, JOGADOR, BOT):

        #defino as marcações usadas para as jogadas // isso é feito qaqui também pois pode haver a necessidade disso ser configurável
        jogadas["SIMBOLO_JOGADA_1"] = jogada_de_inicio[0]
        jogadas["SIMBOLO_JOGADA_2"] = jogada_inimiga[0]

        #aqui inicializo quem vai jogar e em qual ordem usando as funções passadas como argumento desde i início
        if bot_presente[0] == False:
            jogadas["JOGADA_1"] = JOGADOR
            jogadas["JOGADA_2"] = JOGADOR


        if bot_presente[0] == True:
            
            if quantidade_de_bots[0] == 2:
                jogadas["JOGADA_1"] = BOT
                jogadas["JOGADA_2"] = BOT

            elif jogador_comeca[0] == True:
                jogadas["JOGADA_1"] = JOGADOR
                jogadas["JOGADA_2"] = BOT

            else:
                jogadas["JOGADA_1"] = BOT
                jogadas["JOGADA_2"] = JOGADOR

    #aqui eu faço a execução na ordem das subfunções
    print(mensagem_de_config) #imprimo a mensagem de configuração
    definir_config(quantidade_de_bots, bot_presente, jogada_de_inicio, jogador_comeca)#configuro a partida
    gerar_jogo(quantidade_de_bots, bot_presente, jogada_de_inicio, jogador_comeca, jogada_inimiga, JOGADOR, BOT)#gero a partida

#essa função faz as chamadas das funções do jogo principal usando a tabela jogadas configurada anteriormente
def config_jogar():

    jogadas["JOGADA_1"](jogadas["SIMBOLO_JOGADA_1"]) #primeira jogada e sua marcação como argumento
    jogadas["JOGADA_2"](jogadas["SIMBOLO_JOGADA_2"]) #segunda jogada e sua marcação como argumento

