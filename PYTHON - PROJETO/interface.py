#essa função pode traduzir os endereços de uma lista para outra (*D -> 2D)
def access_interface(interface_list, index_, method="get", changes=None): #(lista para qual os endereços serão traduzidos,
                                                                          #2 inteiros dentro da lista que será traduzida (esse campo é 1D - [index_1, index_2]),
                                                                          #indica o método de acesso,
                                                                          #quais mudançãs devem ser feitas) 

    #apenas retorna o valor na posição
    if method == "get":
        return interface_list[index_[0]][index_[1]]

    #modifica e depois retorna o valor na posição
    elif method == "set":
        if changes != None: interface_list[index_[0]][index_[1]] = changes

        return interface_list[index_[0]][index_[1]]


