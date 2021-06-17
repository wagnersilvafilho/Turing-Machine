
#O objetivo desse algoritmo é a implementação de uma MT que reconhece a linguagem consistindo de todas as cadeias de 0's cujo comprimento é uma potência de 2.
#Para tal, a metodologia utilizada foi a criação de funções que representam os estados da MT, uma lista representando a fita magnética com os valores de entrada, e a cabeça de leitura que é representada pela execução da movimentação de indices da lista.

cabeca = 0 #inicialização da cabeça de leitura;
fita = [] #inicialização da lista de entrada

#Cada função retorna uma espécie ID, ou seja, um valor que a representa.

#Do estado Q1 nossa entrada pode ser rejeitada ou ir para o estado Q2. Para passar para o estado Q2, a entrada deve ser válida ('0'), escreve-se o vazio (aqui representado por u) e move-se a cabeça para a direita. Caso a entrada seja diferente de 0, rejeita.
def estadoQ1():
  global cabeca
  global fita
  if fita[cabeca] == '0':
    fita[cabeca] = 'u';
    cabeca += 1 #movimentação da cabeça para a direita
    return 2
  if fita[cabeca] == 'u':
    cabeca += 1 #movimentação da cabeça para a direita
    return 7
  if fita[cabeca] == 'X':
    cabeca += 1
    return 7
   

#Do estado Q2 nossa entrada pode ser aceita caso seja branco, indo para o estado de aceitação. Caso a entrada seja X a cabeça move-se para a direita apenas, permanecendo no mesmo estado, e caso seja 0 é marcada com X, a cabeça move-se para a direita e muda-se para o estado Q3. De acordo com a MT, caso esse estado leia branco significa que ele passou por toda a entrada da fita e não encontrou um '0' ou um 'X', sendo assim aceitando a entrada.
def estadoQ2():
  global cabeca
  global fita
  if fita[cabeca] == '0':
    fita[cabeca] = 'X'; #marcação na fita
    cabeca += 1 #movimentação da cabeça para a direita
    return 3
  if fita[cabeca] == 'u':
    cabeca += 1 #movimentação da cabeça para a direita
    return 6
  if fita[cabeca] == 'X':
    cabeca += 1
    return 2


#Do estado Q3 temos que caso a entrada seja 0, a cabeça move-se para a direita e vamos para o estado 4. No caso de branco, move-se a cabeça para a esquerda e vamos para o estado 5, e no caso da posição já estar marcada com X continua-se no mesmo estado até a entrada ser diferente de 'X'.
def estadoQ3():
  global cabeca
  global fita
  if fita[cabeca] == '0':
    cabeca += 1 #movimentação da cabeça para a direita
    return 4
  if fita[cabeca] == 'u':
    cabeca -= 1 #movimentação da cabeça para a esquerda
    return 5
  if fita[cabeca] == 'X':
    cabeca += 1
    return 3

#Já no estado Q4, caso minha entrada já esteja marcada, apenas movo a cabeça da fita, mantendo-se no mesmo estado. Quando tem-se vazio neste estado, a entrada é rejeitada. Caso tenha-se um zero, a posição é marcada com X e volta-se para o estado Q3.
def estadoQ4():
  global cabeca
  global fita
  if fita[cabeca] == 'X':
    cabeca += 1
    return 4
  if fita[cabeca] == '0':
    fita[cabeca] = 'X'
    cabeca += 1
    return 3
  if fita[cabeca] == 'u':
    cabeca += 1
    return 7
    
#No estado Q5 existe um Loop que mantém o estado executando até a cabeça chegar ao branco (entrada). Quando chega, significa que temos o ínicio da fita, portanto inicia-se novamente a leitura a partir do estado Q2.
def estadoQ5():
  global cabeca  
  global fita
  if fita[cabeca] == 'X':
    cabeca -= 1 #movimentação da cabeça para a esquerda
    return 5
  if fita[cabeca] == '0':
    cabeca -= 1 #movimentação da cabeça para a esquerda
    return 5
  if fita[cabeca] == 'u':
    cabeca += 1 #movimentação da cabeça para a direita
    return 2

def aceita():
  print ('A entrada foi aceita.\n') #funcao que printa que a entrada aceita
  print ('Final: ', fita, '\n') #fita final apos o termino da execução

def rejeita():
  print ('A entrada foi rejeitada.\n') #funcao que printa a entrada rejeitada
  print ('Final: ', fita, '\n') #fita final apos o termino da execução
    
estados = { 
   1: estadoQ1,
   2: estadoQ2,
   3: estadoQ3,
   4: estadoQ4,
   5: estadoQ5,
   6: aceita,
   7: rejeita
} #Estados da MT em estrutura

entrada = input('\nEntre com os valores da cadeia de zeros: ') #aqui o usuario entra com a linguagem, é a fita de entrada
fita = list(entrada) + ['u'] #adicionado uma entrada em branco ao final da fita, indicando o fim das entradas da mesma
print ('\n')
proxEstado = 1
proxFuncao = estadoQ1 #o estado inicial é Q1, portanto é o primeiro ao ser chamado passando a fita como argumento.

while (proxFuncao != estados[6] and proxFuncao != estados[7]): #Este é o laço de repetição que garante a execução enquanto não rejeitado ou aceito.
  print (f'Estado Q{proxEstado}: \n') #print do estado atual da leitura
  print (fita[:cabeca] + [f'q{proxEstado}'] + fita[cabeca:], "\n\n") #print da fita completa apos a execucao do estado atual
  proxEstado = proxFuncao() #passado o retorno da função (ID mencionado no início) para acionar o próximo estado
  proxFuncao = estados[proxEstado] #a função é executada recebendo o que retorna do estado

proxFuncao() #execucao das funcoes




