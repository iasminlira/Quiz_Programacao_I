import json
import random
import operator

nickname = str()
dictRanking = {}
dictPerguntas = {}

#funcao para pegar os 10 jogadores com melhor pontuacao
def score():
    with open("Ranking.txt") as ff:
        data = ff.read()
        ja = json.loads(data)
        dictRanking = (ja)
        sortedRanking= dict(sorted(dictRanking.items(), key=operator.itemgetter(1),reverse=True))
        x = 0
        while x <= 9:
            key_list = list(sortedRanking)
            a_key = key_list[x]
            key = str(a_key)
            print(str(x+1)+" - "+a_key+" : "+str(sortedRanking[a_key]))
            x+=1

#funcao para buscar as perguntas por número/codigo da alternativa
def buscaPergunta():
    with open("Perguntas.txt", encoding="utf8") as ff:
        data = ff.read()
    js = json.loads(data)
    dictPerguntas = js
    codigoAlternativa = (input('Digite o numero da questão que deseja buscar: '))
    if codigoAlternativa in dictPerguntas:
            x = codigoAlternativa
            dificuldade = (dictPerguntas[x][6])
            if dificuldade == "1":
                NivelDificuldade = str("Facil")
            elif dificuldade == "2":    
                NivelDificuldade = str("Medio")
            elif dificuldade == "3":    
                NivelDificuldade = str("Dificil")

            #mostrar a pergunta que o usuario decidiu buscar
            print(x+')'+str(dictPerguntas[x][0])+'?'+'  Nivel de Dificudade:'+str(NivelDificuldade))
            print()
            print(dictPerguntas[x][1])
            print(dictPerguntas[x][2])
            print(dictPerguntas[x][3])
            print(dictPerguntas[x][4])
            print('Resposta: '+str(dictPerguntas[x][5]))
    else:
        print('A pergunta não está no banco de dados!')

#funcao para remover uma pergunta existente no registro
def removerPergunta():
    with open("Perguntas.txt") as ff:
        data = ff.read()
    js = json.loads(data)
    dictPerguntas = js
    codigoAlternativa = (input('Digite o numero da questão que deseja remover: '))
    if codigoAlternativa in dictPerguntas:
        dictPerguntas.pop(codigoAlternativa)
        with open("Perguntas.txt", "w") as fa:
            fa.write(json.dumps(dictPerguntas))
            fa.close
        print('Pergunta removida com sucesso!')
    else:
         print('Questão não está cadastrada, deseja cadastrar uma nova questão digite "S" para sim e "N" para não: ')
         r = input().upper()
         if r == 'S':
            cadastrarPergunta()
         elif r == 'N':
            print('')
            return

#funcao para alterar uma pergunta existente no registro
def alterarPergunta():
    with open("Perguntas.txt") as ff:
        data = ff.read()
    js = json.loads(data)
    dictPerguntas = js
    codigoAlternativa = (input('Digite o numero da questão que deseja Alterar: '))
    if codigoAlternativa in dictPerguntas:
        enuciado = input("Digite o enuciado da questão: ")
        questao = enuciado.translate(str.maketrans('','','#$%&:;^_`{|}~'))
        alternativaA = 'a)'+input("Digite a altenativa 'a': ")
        alternativaB = 'b)'+input("Digite a altenativa 'b': ")
        alternativaC = 'c)'+input("Digite a altenativa 'c': ")
        alternativaD = 'd)'+input("Digite a altenativa 'd': ")
        alternativaCorreta = input('Digite a alternativa correta: ')
        dificudadeAlternativa = (input('Digite a dificuldade de 1 a 3 da questão: '))
        dictPerguntas[codigoAlternativa] = [questao, alternativaA, alternativaB, alternativaC, alternativaD, alternativaCorreta, dificudadeAlternativa]
        with open("Perguntas.txt", "w") as fa:
            fa.write(json.dumps(dictPerguntas))
            fa.close
    else:
        print('Questão não está cadastrada, deseja cadastrar uma nova questão digite "S" para sim e "N" para não: ')
        r = input().upper()
        if r == 'S':
            cadastrarPergunta()
        elif r == 'N':
            print('')
            return

#funcao para cadastrar uma pergunta no registro
def cadastrarPergunta():
    with open("Perguntas.txt") as ff:
        data = ff.read()
    js = json.loads(data)
    dictPerguntas = js
    f = open("Perguntas.txt", "r")
    codigoAlternativa = (input('Digite um numero para essa questão: '))
    if  codigoAlternativa in dictPerguntas:
        print('numero da questão já existente tente novamente')  
    else:
        #pega os inputs, os coloca num dicionario e atualiza o arquivo de perguntas.txt com a nova pergunta inserida pelo usuário
        enuciado = input("Digite o enuciado da questão: ")
        questao = enuciado.translate(str.maketrans('','','#$%&:;^_`{|}~'))
        alternativaA = 'a)'+input("Digite a altenativa 'a': ")
        alternativaB = 'b)'+input("Digite a altenativa 'b': ")
        alternativaC = 'c)'+input("Digite a altenativa 'c': ")
        alternativaD = 'd)'+input("Digite a altenativa 'd': ")
        alternativaCorreta = input('Digite a alternativa correta: ')
        dificudadeAlternativa = (input('Digite a dificuldade de 1 a 3 da questão: '))
        dictPerguntas[codigoAlternativa] = [questao, alternativaA, alternativaB, alternativaC, alternativaD, alternativaCorreta, dificudadeAlternativa]
        with open("Perguntas.txt", "w") as fa:
            fa.write(json.dumps(dictPerguntas))
            fa.close

#funcao para cadastrar o jogador
def cadastrarJogador():
    with open("Ranking.txt") as ff:
        data = ff.read()
        dc = data.replace("'", "\"")
        ja = json.loads(data)
        dictRanking = (ja)
    nome = input("Digite seu Nickname: ")
    print('----------------------------------------------------------------------------------------------------')
    nickname = nome
    pontuacao = 0
    dictRanking[nome] = pontuacao
    with open("Ranking.txt", "w") as fa:
            fa.write(json.dumps(dictRanking))
            fa.close
    return nome

#funcao para carregar as perguntas existentes no registro 
def carregaPerguntas(nome):
    with open("Perguntas.txt", encoding="utf8") as ff:
        data = ff.read()
    js = json.loads(data)
    dictPerguntas = js
    with open("Ranking.txt") as fr:
        data = fr.read()
        ja = json.loads(data)
        dictRanking = (ja)
    f = open("Perguntas.txt", "r")
    fa = open("Ranking.txt", "a")
    k= 1
    i = len(dictPerguntas)
    for x in dictPerguntas:
        y= 0
        #gera randomicamente 10 perguntas
        r = random.sample(range(1, i), 10)
        #parte do codigo que mostra as perguntas
        while k <= 10:
            x = r[y]
            x = str(x)
            dificuldade = (dictPerguntas[x][6])
            if dificuldade == "1":
                NivelDificuldade = str("Facil")
            elif dificuldade == "2":    
                NivelDificuldade = str("Medio")
            elif dificuldade == "3":    
                NivelDificuldade = str("Dificil")
            print(x+')'+str(dictPerguntas[x][0])+'?'+'  Nivel de Dificudade:'+str(NivelDificuldade))
            print()
            print(dictPerguntas[x][1])
            print(dictPerguntas[x][2])
            print(dictPerguntas[x][3])
            print(dictPerguntas[x][4])
            resposta = str(dictPerguntas[x][5]).upper()
            dificuldade = (dictPerguntas[x][6])
            valor = dificuldade.translate(str.maketrans('','','#$%&:;^_`{|}~'))
            resultado = input("Resposta: ").upper()
            y+= 1
            if resultado == resposta: 
                #parte do codigo onde é colocado apontuacao de cada jogador
                with open("Ranking.txt", "w") as fa:
                    pontuacao = int(dictRanking[nome])    
                    pontuacao += int(valor)
                    dictRanking[nome] = pontuacao
                    fa.write(json.dumps(dictRanking))
                    fa.close
                print("resposta correta")
                print('----------------------------------------------------------------------------------------------------')
                print()
            else:
                print("Resposta incorreta")
                print('----------------------------------------------------------------------------------------------------')
                print()
            k+= 1
    f.close()
    return 


#Menu de iniciação do jogo.
print(''' 
Bem vindo ao Quizzz!
Caso deseje iniciar o Quiz digite 'S' para sim e 'N' para não:
''')
escolha = input().upper()
print('----------------------------------------------------------------------------------------------------')

#Menu de escolhas do jogo.
while escolha != ('N'):
  if escolha == ('S').upper():
    print('''Escolha uma das opções a seguir:
    1 - Iniciar
    2 - Perguntas
    3 - Score
    4 - Sair
    ''')
    opcao = input()
    print('----------------------------------------------------------------------------------------------------')
    print()

    #Acao de cadastrar o jogador e dar start no jogo ao escolher a opcao 1
    if opcao == '1':
        carregaPerguntas(cadastrarJogador())
        print('----------------------------------------------------------------------------------------------------')
        print()

    #Menu de perguntas do jogo ao selecionar a opao 2 no menu de escolhas.    
    elif opcao == '2':
        print('''Escolha uma das opções a seguir:
        1 - Adicionar Pergunta
        2 - Alterar Pergunta
        3 - Remover Pergunta 
        4 - Buscar Pergunta
        ''')
        resposta = input()
        print('----------------------------------------------------------------------------------------------------')
        print()

        #sequencia de açoes seguindo a ordem do menu de perguntas(Adicionar, Alterar, Remover e Buscar Pergunta)
        if resposta == '1':
            cadastrarPergunta()
            print('----------------------------------------------------------------------------------------------------')
            print()
            
        elif resposta == '2':
            alterarPergunta()
            print('----------------------------------------------------------------------------------------------------')
            print()
            
        elif resposta == '3':
            removerPergunta()
            print('----------------------------------------------------------------------------------------------------')
            print()
            
        elif resposta == '4':
            buscaPergunta()
            print('----------------------------------------------------------------------------------------------------')
            print()


    #Acao de mostrar o score do jogador
    elif opcao == '3':
        score()
        print('----------------------------------------------------------------------------------------------------')
        print()

    #Acao de sair do jogo    
    elif opcao == '4':
        print('----------------------------------------------------------------------------------------------------')
        print()
        exit()
        
  elif escolha == ('P').upper():
    cadastrarPergunta()  
    continue