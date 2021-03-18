# Jogo_da_velha_MELHORADO

Esse programa é um jogo da velha feito totamente em python. Ele possui 3 funcionalidades básicas: o jogo da velha em si, configuração de partida e um bot (que não faz uso de machine learnig).

Versão do python utilizada: Python 3.9.1 

Ambiente de execução: Terminal de comandos

Como executar: abra o seu terminal, escreva python e em seguida o caminho absoluto do arquivo jogo_da_velha.py

Esse software utiliza a licença MIT.

EXTRA:

Explicação sobre o código:
  Existem 4 arquivos, cada um com uma funcionalidade. O jogo_da_velha.py contém o jogo em si e uma lista que mapeia as posições no jogo. O bot.py possui todas as funções e lógicas neessárias para o funcionamento do bot no jogo. Config.py recebe as entradas do usuário e gera a configuração de uma partida. O interface.py contem apenas uma função, que é usado pelo bot e pelo jogo_da_velha, e faz a tradução de um index de uma lista para outra. (explicações mais detalhadas estão nos comentários dcódigo)
  
  
 
Detalhes importantes:
  Como o python não possui ponteiros e optei por não usar classes, existe um pequeno "hack". Em algumas funções eu queria que o cada uma tivesse suas próprias variáveis e que outras funções podessem modificá-las (func_1 tem variáveis locais -> chamadas sebsequentes de outras funções dentro da func_1 modificam as variáveis locais de func_1 -> todas as funções trabalham com as variáveis de func_1 por maio de referência). Isso podia ser facilmente atingido usando ponteiros presentes, por exemplo, em C/C++, porém o python não tem. Uma maneira seria usar classes e passar a classe (o objeto na verdade) como argumento para em seguida acessar os atributos (func_1(obj) -> obj.atributo = "o que quiser") (pode ser usando um set() também). Ou poderia criar uma lista de um único index e toda vez que ele é passado como argumento ele funciona como referência (semelhante a passar um objeto como argumento), assim a variável sempre que a variável é alterada por outra função ela também altera a original.
  Se alguém tiver um sugestão mais elegante para resolver esse problema, fique a vontade!
  
  
Curiosidade:
  Para usar refências em classes você passar como argumento o objeto e não os atributos (senão eles acabam funcionando igual variáveis normais) para em seguida chamar os atributos. Também é possível usar as listas de 1 index e passar como referência a lista (o atributo é uma lista de 1 index).
 

