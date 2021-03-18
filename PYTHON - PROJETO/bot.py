import random

import interface

def bot_jogar(tabela_jogo, lista_interface, minha_jogada_vez):

    jogada_inimiga = "_" #inicializo a variável

    #configuro a jogada inimiga baseada na minha
    if minha_jogada_vez == "X":
        jogada_inimiga = "O"

    else:
        jogada_inimiga = "X"

    #lista de retas vencedoras (esses serão RETIRADOS na atualização)
    #"-> |^ \ /" : as retas abaixo foram representadas assim: esquerda p/ direita, baixo p/ cima, diagonal decrescente e depois crescente
    lista_retas_vencedoras = [

        [1, 2, 3], # 1, 2 , 3
        [4, 5, 6], # 4, 5, 6
        [7, 8, 9], # 7, 8, 9

        [1, 4, 7], # 1, 4 , 7
        [2, 5, 8], # 2, 5 , 8
        [3, 6, 9], # 3, 6 , 9

        [7, 5, 3], # 7, 5 , 3
        [1, 5, 9] # 1, 5 , 9

    ]

    #lista de retas vencedoras inimigas (esses serão RETIRADOS na atualização)
    
    lista_retas_vencedoras_inimigas = [

        [1, 2, 3], # 1, 2 , 3
        [4, 5, 6], # 4, 5, 6
        [7, 8, 9], # 7, 8, 9

        [1, 4, 7], # 1, 4 , 7
        [2, 5, 8], # 2, 5 , 8
        [3, 6, 9], # 3, 6 , 9

        [7, 5, 3], # 7, 5 , 3
        [1, 5, 9] # 1, 5 , 9

    ]


    #lista de espaços vazios (esses serão ADICIONADOS na atualização)
    lista_de_espacos_vazios = []



    #atualiza a lista com valores válidos
    def bot_atualiza_lista_retas_vencedoras(lista_avaliada, jogada_avaliada):
        
        i = 0
        while i < len(lista_avaliada):
            #print("i : ", i)

            try:
                j = 0
                while j < len(lista_avaliada[i]):
                    #print('j : ', j)

                    valor_da_pos = interface.access_interface(tabela_jogo, lista_interface[lista_avaliada[i][j]], "get")

                    #se a posição for vazia não faça nada
                    if valor_da_pos == "_":
                        pass
                    
                    #se estiver ocupada pela jogada avaliada, apenas tire a posição
                    elif valor_da_pos == jogada_avaliada:
                        del lista_avaliada[i][j]
                        continue

                    #esse caso só acontece se a posição estiver ocupado pelo inimigo, nesse caso tire a reta da lista
                    else:
                        del lista_avaliada[i] #usar uma variável com if depois (altero uma var e depois avalio)
                        raise Exception() #isso gera um erro e pula para o except ->

                    j = j + 1

            # -> no except ele pula o incremento // como eu tirei uma linha, ele deve recomeççar o loop pela mesma linha
            except:
                continue

            i = i + 1

        #ordena a lista baseado na tamanho de cada célula
        lista_avaliada.sort(key = len)

    #essa função preenche a lista de espaços vazios com possíveis posições
    def preenche_listas_vazias(lista_avaliada):
        x = 0
        while x < 9:

            if interface.access_interface(tabela_jogo, lista_interface[x + 1], "get") == "_":
                lista_de_espacos_vazios.append(x + 1)

            #print('X : ', x)
            #print('access_interface : ', interface.access_interface(tabela_jogo, lista_interface[x + 1], "get"))
            x = x + 1

    #essa função define um conjunto de retas de mesmo tamanho na lista de retas // retorna im index máximo (estão ordenadas por tamanho, fica facil definir um conjunto)
    def definir_limite_de_prioridade(lista_avaliada):
        pos_minima = 0
        prioidade = len(lista_avaliada[pos_minima])
        pos_maxima = 0

        #print('primeira pos da lista : ', lista_avaliada[pos_minima])
        #print('prioridade : ', prioidade)

        while True:
            try:
                #se a posição tem o mesmo tamanho do primeira célula (prioridade)
                if prioidade == len(lista_avaliada[pos_maxima]):
                    pos_maxima = pos_maxima + 1
                    continue

                #se não tiver o mesmo tamanho, saia do loop e coloque a prioridade no valor antigo
                else:
                    pos_maxima = pos_maxima - 1
                    break
            
            #se essa posição estiver fora to tamanho da lista, coloque a prioridade no valor antigo e saia do loop
            except IndexError:
                pos_maxima = pos_maxima - 1
                break

        return pos_maxima



        
    def arvore_de_desicoes():
        #árvore de decições
            #se ganho em uma jogada (primeira posição com apenas 1 espaço) - jogue
            if lista_retas_vencedoras != []:
                if len(lista_retas_vencedoras[0]) == 1:
                    interface.access_interface(tabela_jogo, lista_interface[lista_retas_vencedoras[0][0]], "set", minha_jogada_vez)
                    return 1


            #se o inimigo ganha em 1 jogada - impeça-o (só chego aqui se não puder ganhar direto)
            if lista_retas_vencedoras_inimigas != []:
                if len(lista_retas_vencedoras_inimigas[0]) == 1:
                    interface.access_interface(tabela_jogo, lista_interface[lista_retas_vencedoras_inimigas[0][0]], "set", minha_jogada_vez)
                    return 1


            #como eu não posso ganhar nem o inimgo, qual a menor reta vencedora que posso preencher
            if  lista_retas_vencedoras != []:

                reta_maxima_possivel = definir_limite_de_prioridade(lista_retas_vencedoras)
                pos_maxima_na_reta = len(lista_retas_vencedoras[0])

                #print('reta_maxima_possivel : ', reta_maxima_possivel, ' / pos_maxima_na_reta : ', pos_maxima_na_reta - 1)

                reta_escolhida = random.randint(0, reta_maxima_possivel)
                pos_escolhida = random.randint(0, pos_maxima_na_reta - 1)

                #print('reta_escolhida : ', reta_escolhida, ' / pos_escolhida : ', pos_escolhida)

                index_escolhido = lista_retas_vencedoras [reta_escolhida] [pos_escolhida] 

                interface.access_interface(tabela_jogo, lista_interface[index_escolhido], "set", minha_jogada_vez)
                return 1


            #se não houver reta vencedora, escolha qualquer espaço em branco
            if lista_retas_vencedoras == [] and lista_retas_vencedoras_inimigas == []:
                tamanho = len(lista_de_espacos_vazios)
                pos_escolhida = random.randint(0, tamanho - 1)
                interface.access_interface(tabela_jogo, lista_interface[ lista_de_espacos_vazios [pos_escolhida] ], "set", minha_jogada_vez)
                return 1


    #essa função executa  as subfunções na ordem desejada
    def execucao():
        bot_atualiza_lista_retas_vencedoras(lista_retas_vencedoras, minha_jogada_vez)
        bot_atualiza_lista_retas_vencedoras(lista_retas_vencedoras_inimigas, jogada_inimiga)
        preenche_listas_vazias(lista_de_espacos_vazios)

        #print('posições de prioridade : ', definir_limite_de_prioridade(lista_retas_vencedoras))
        #print("retas vencedoras: ", lista_retas_vencedoras)
        #print("retas vencedoras inimigas: ", lista_retas_vencedoras_inimigas)
        #print("lista de espaços vazios: ", lista_de_espacos_vazios)

        arvore_de_desicoes()

    #executa todas as funções
    execucao()
