import bot
import interface
import config

#essa lista mapeia a lista tabela_jogo (a tradução é feita usando a função do interface)
lista_interface = {


    7: [0,0],
    8: [0,1],
    9: [0,2],
    
    4: [1,0],
    5: [1,1],
    6: [1,2],
    
    1: [2,0],
    2: [2,1],
    3: [2,2]



}


#defino uma mensagem de boas vindas
def bem_vindo():

    #crio uma variável com uma mensagem de boas vindas explicando o programa e imprimo na tela
    msg_boas_vindas = '''

    Esse programa é um jogo da velha.
    As linhas e colunas possuem as seguintes posições (eles são parecidas com as posições do teclado numérico)

         7    8    9 

         4    5    6 
         
         1    2    3

    Divirta-se!!!

    '''
    print(msg_boas_vindas, end="\n\n\n")



#crio uma matriz representando os espaços do jogo da velha // ele vai servir principalmente para poder referenciar as coordenadas com mais facilidade
#cada item da lista possui uma outra lista dentro
tabela_jogo = [

    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]

]


#defino uma função para imprimir o jogo na tela
def imprimir_jogo():

    #pula duas linha no começo da impressão
    print("\n\n")
    #acessa a linha int(tabela_jogo)
    for linha in range(len(tabela_jogo)): #o range() cria um objeto com uma lista de números que começa no zero e o len() pega o tamanho

        #acessa cada coluna ou item
        for coluna in range(len(tabela_jogo[linha])):
            #imprime cada item individualmente // \t - tab // "   " - espaço entre itens // end="" - não pule de linha
            print("\t", tabela_jogo[linha][coluna], "   ", end="")

        #ao terminar a linha da tabela pule uma linha na tela
        print("\n")

    #ao terminar a tabela pule 2 linhas
    print("\n\n")
    

#crio contadores para determinar o vencedor em cada função (ou seja, cada função que possui uma declaração poussi contadores próprios)
#usei como no fomato de lista porque permiti usar essas variáveis como referência (value by reference)
#cada função de checagem possui seus contadores -> envia por referência à função verifica() -> que em seguida passa para a reinicializa_contadores()
#parecido com o uso de pomteiros duplos

#defino uma função para determinar um vencedor ou a impossibilidade de um (quando dá velha)
def vencedor_ou_velha():
    
    #defino uma função que reinicializa os contadores, caso contrário iriam incrementar incorretamente, quebrando as condições
    def reinicializa_contador(contador_X, contador_O, contador_espacos_cheios):
        
        contador_X[0] = 0
        contador_O[0] = 0
        contador_espacos_cheios[0] = 0
    

    #essa função verifica os contadores. Se houver vencedor: imprima uma mensagem e termine o programa. Se ninguém ganhar, só reinicie os contadores
    def verifica(contador_X, contador_O, contador_espacos_cheios):
        
        if contador_X[0] == 3:
            print("\nO jogador X ganhou!")
            raise SystemExit #gera em "erro" que executa a saída do programa

        elif contador_O[0] == 3:
            print("\nO jogador O ganhou!")
            raise SystemExit

        elif contador_espacos_cheios[0] == 9:
            print("\nDeu velha!")
            raise SystemExit
            
        else:
            reinicializa_contador(contador_X, contador_O, contador_espacos_cheios) #chama a função'''

    #essa função verifica linha por linha no jogo incrementando os contadores de "X" ou "O"
    def vencedor_linha(contador_X, contador_O, contador_espacos_cheios):

        #acessa a linha
        for linha in range(len(tabela_jogo)):

            #acessa os itens da linha
            for item in range(len(tabela_jogo[linha])):

                if tabela_jogo[linha][item] == "X":
                    contador_X[0] = contador_X[0] + 1

                elif tabela_jogo[linha][item] == "O":
                    contador_O[0] = contador_O[0] + 1
                
            
            verifica(contador_X, contador_O, contador_espacos_cheios) #chama a função de verificar, deve ser feita a cada linha para manter os contadores corretos e poder fazer a verificação correta
            
            

    #mesma a coisa que o da linha, mas esse verifica cada coluna
    def vencedor_coluna(contador_X, contador_O, contador_espacos_cheios):

        for coluna in range(len(tabela_jogo[0])): #descobre quantas colunas tem (itens na linhas), como é 3x3 posso usar qualquer linha

            for item in range(len(tabela_jogo)): #acessa os itens de cada coluna

                if tabela_jogo[item][coluna] == "X":
                    contador_X[0] = contador_X[0] + 1

                elif tabela_jogo[item][coluna] == "O":
                    contador_O[0] = contador_O[0] + 1
                
            
            verifica(contador_X, contador_O, contador_espacos_cheios)#mesmo princípio de antes
          
            

    #esse verifica vencedores na diagonal
    def vencedor_diagonal(contador_X, contador_O, contador_espacos_cheios):

        #variável que decresce para a diagonal crescente
        j = 2

        #diagonal decrescente
        #como só tem 3 e as coordenadas são repitidas (1-1,2-2,3-3), cheguei nisso: um loop que repete 3 vezes e a variável i é igual nas coordenadas
        for i in range(3):
            if tabela_jogo[i][i] == "X":
                contador_X[0] = contador_X[0] + 1

            elif tabela_jogo[i][i] == "O":
                contador_O[0] = contador_O[0] + 1

        verifica(contador_X, contador_O, contador_espacos_cheios) #só verifica depois de "olhar" toda a diagonal
        
        #diagonal crescente
        #mesma coisa de antes, mas dessa vez uma das coordenadas começava no máximo valor possível e decrementava em 1 a cada mudança de posição
        
        for i in range(3):
            
            if tabela_jogo[i][j] == "X":
                contador_X[0] = contador_X[0] + 1

            elif tabela_jogo[i][j] == "O":
                contador_O[0] = contador_O[0] + 1

            j = j - 1 #sempre decrementa a cada loop

        verifica(contador_X, contador_O, contador_espacos_cheios)
        

    #esse verifica a impossibilidade de vencedores ("Deu velha!")
    #basicamente funciona assim: se ninguém ganhar o jogo -> ele é executado (se alguém ganhar a finalização é realizada antes) -> se todas as posições estiverem ocupadas (e como o programa não foi finalizado) --
    #--> só podemos concluir que ninguém ganhou e que não existem mais jogadas possíveis -> "DEU VELHA!"
    def velha(contador_X, contador_O, contador_espacos_cheios):
        #acessa linha
        for linha in range(len(tabela_jogo)):

            #acessa o item
            for item in range(len(tabela_jogo[linha])):

                if tabela_jogo[linha][item] == "X" or tabela_jogo[linha][item] == "O": #identifica se a posição está preenchida ou não
                    contador_espacos_cheios[0] = contador_espacos_cheios[0] + 1
                
        verifica(contador_X, contador_O, contador_espacos_cheios) #so verifica depois de "olhar" todo o jogo
        

    #aqui são cahamdas as funções dentro do verifica() na ordem que eu quero a execução
    vencedor_linha([0], [0], [0])
    vencedor_coluna([0], [0], [0])
    vencedor_diagonal([0], [0], [0])
    velha([0], [0], [0]) #está no final para garantir que o programa não dê velha mesmo tendo um vencedor
        
        
#defino uma função que mostra qual é o jogador da vez(recebendo como um argumento) e escerve a jogada
def escrever_vez(jogada_vez):
    #variável que recebe as corrdenadas em formato de string para poder usar a função split() do python
    coord_pos = ""

    #loop infinito
    while True:

        #tratamento de erro
        try:
            coord_pos = input("Escreva em qual posição você deseja escrever " + jogada_vez + " : ") #imprime a mensagen de jogada

            #tranforma os itens em inteiros // tranforma os itens da lista de strings em inteiros para poderem ser usados
            coord_pos = int(coord_pos) #erro gera um ValueError

            if coord_pos < 1 and coord_pos > 9: #se o usuário não der a quantidade exata de coordenadas gere um erro
                raise Exception()

            #avalie se a posição não está ocupada para prosseguir(break)
            if  interface.access_interface(tabela_jogo, lista_interface[coord_pos], "get") == "_":
                break
            else:
                print("\nEspaço já ocupado! Escolha outra coordenada\n")

        #mensagem de tratamento de erro
        except ValueError:
            print("\nEntrada de dados inválida! Tente novamente com apenas uma posição numérica\n")
        except Exception:
            print("\nVocê não passou uma cooredenada válida. Tente novamente com apenas uma posição numérica\n")


    interface.access_interface(tabela_jogo, lista_interface[coord_pos], "set", jogada_vez) #escreve a jogada na tabela_jogo


#defino uma função com todas as funções principais para a jogo
def vez_jogador(var_vez):
    escrever_vez(var_vez)
    imprimir_jogo()
    vencedor_ou_velha()

def vez_bot(var_vez):
    bot.bot_jogar(tabela_jogo, lista_interface, var_vez)
    imprimir_jogo()
    vencedor_ou_velha()

#defino uma main() que será chamada para a execução do programa 
def main():
    bem_vindo() #mostro uma mensagem de boas-vindas
    config.iniciar_config(vez_jogador, vez_bot) #configuro o jogo
    imprimir_jogo() #imprimo o jogo

    while True:
        config.config_jogar() #efetivamente executo o jogo


#função main é chamada
main()



