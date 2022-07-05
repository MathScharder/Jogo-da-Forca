#!/usr/bin/env python
#encoding: UTF-8

import os
import gerenciadorDB as GDB
import string
from termcolor import cprint

def testeFinal(mascara):
    '''
    Função para fazer o teste de validade do jogo
    '''
    for i in mascara:
        if i == '_':
            teste =  True
        else:
            teste = False   
    
    return teste

def stickman(letrasErradas, mascara, id, dificuldadeExtenso, qtdTentativas,qtdJogadas,qtdAcertos):
    if len(letrasErradas) == 0:
        print("+----+    " + dificuldadeExtenso + "- ID: " + id)
        print("  |  |    " + "Tentativas: " + str(qtdTentativas))
        print("     |    " + "Erros: " + str((qtdJogadas - qtdAcertos)))
        print("     |    " + "Certos: " + str(qtdAcertos))
        print("     |    ")
        print("     |    ")
        print("=======")    
    elif len(letrasErradas) == 1:
        print("+----+    " + dificuldadeExtenso + "- ID: " + id)
        print("  |  |    " + "Tentativas: " + str(qtdTentativas))
        print("  O  |    " + "Erros: " + str((qtdJogadas - qtdAcertos)))
        print("     |    " + "Certos: " + str(qtdAcertos))
        print("     |")
        print("     |")
        print("=======")
    elif len(letrasErradas) == 2:
        print("+----+    " + dificuldadeExtenso + "- ID: " + id)
        print("  |  |    " + "Tentativas: " + str(qtdTentativas))
        print("  O  |    " + "Erros: " + str((qtdJogadas - qtdAcertos)))
        print("  |  |    " + "Certos: " + str(qtdAcertos))
        print("  |  |")
        print("     |")
        print("=======")
    elif len(letrasErradas) == 3:
        print("+----+    " + dificuldadeExtenso + "- ID: " + id)
        print("  |  |    " + "Tentativas: " + str(qtdTentativas))
        print("  O  |    " + "Erros: " + str((qtdJogadas - qtdAcertos)))
        print(" [|  |    " + "Certos: " + str(qtdAcertos))
        print("  |  |")
        print("     |")
        print("=======")
    elif len(letrasErradas) == 4:
        print("+----+    " + dificuldadeExtenso + "- ID: " + id)
        print("  |  |    " + "Tentativas: " + str(qtdTentativas))
        print("  O  |    " + "Erros: " + str((qtdJogadas - qtdAcertos)))
        print(" [|] |    " + "Certos: " + str(qtdAcertos))
        print("  |  |")
        print("     |")
        print("=======")
    elif len(letrasErradas) == 5:
        print("+----+    " + dificuldadeExtenso + "- ID: " + id)
        print("  |  |    " + "Tentativas: " + str(qtdTentativas))
        print("  O  |    " + "Erros: " + str((qtdJogadas - qtdAcertos)))
        print(" [|] |    " + "Certos: " + str(qtdAcertos))
        print("  |  |")
        print(" [   |")
        print("=======")
    elif len(letrasErradas) == 6:
        print("+----+    " + dificuldadeExtenso + "- ID: " + id)
        print("  |  |    " + "Tentativas: " + str(qtdTentativas))
        print("  O  |    " + "Erros: " + str((qtdJogadas - qtdAcertos)))
        print(" [|] |    " + "Certos: " + str(qtdAcertos))
        print("  |  |")
        print(" [ ] |")
        print("=======")
      
def palavraEscolhida(*lista):
    return lista[0],lista[1],lista[3],lista[4],lista[5]
            
def jogo():
    '''
    Função de Inicialização do Jogo
    '''
    #Preparação das variáveis
    mascara = []
    letrasCertas = []
    letrasErradas = []
    tentativas = 0
    print('Qual a Dificuldade que gostaria de jogar? 1 - Fácil; 2 - Médio; 3 - Difícil')
    dificuldade = (int)(input('Sua opção: '))
    if dificuldade == 1:
        dificuldadeExtenso = 'Fácil'
    elif dificuldade == 2:
        dificuldadeExtenso = 'Médio'
    else:
        dificuldadeExtenso = 'Difícil'
        
    id,palavra,qtdTentativas,qtdJogadas,qtdAcertos = palavraEscolhida(*GDB.escolher_palavra(dificuldade))
   
    
    #Criação da Mascara
    for i in range(len(palavra)):
        mascara.append('_')
    
    #Seção do Jogo
    while tentativas < qtdTentativas: 
        os.system('cls' if os.name == 'nt' else 'clear') 
        #Região de Print da Tela
        stickman(letrasErradas, mascara,str(id),dificuldadeExtenso,(qtdTentativas-tentativas),qtdJogadas,qtdAcertos)
        print('\n')
        for i in range(len(palavra)):
            print(mascara[i] ,end=' ')
        print('\n\nLetras Certas:',end='')
        for i in range(len(letrasCertas)):
            cprint( letrasCertas[i], 'green',end='')
        print('\nLetras Erradas:',end='')
        for i in range(len(letrasErradas)):
            cprint( letrasErradas[i], 'red',end='')

        #Teste Inicial
        if testeFinal(mascara) == False:
            print('\n\nParabéns você ganhou!!!\n a palavra é:' + palavra)
            input('\n>>> Pressione para sair desta Tela <<<')
            GDB.retornar_palavra(id,palavra,dificuldade,qtdTentativas,(qtdJogadas+1),(qtdAcertos+1))
            break
        
        #Região de Interação com o usuário
        print('\n')
        userChoice = input('Digite:\n1 - para Letra;\n2 - para a Palavra Toda\n Sua Opção: ')
        if userChoice == '1':
            letra = input('\nQual letra deseja tentar? ')
            #Verificar se a Letra é correta ou Errada e trocar na máscara
            if letra.upper() in palavra:
                letrasCertas.append(letra)
                for index, i in enumerate(palavra):
                    if letra.upper() == i.upper():
                        mascara[index] = palavra[index].upper()
            else:
                letrasErradas.append(letra)      
            
            if tentativas == qtdTentativas:
                if testeFinal(mascara) == False:
                    print('\n\nParabéns você ganhou!!!\n a palavra é:' + palavra)
                    input('\n>>> Pressione para sair desta Tela <<<')
                    GDB.retornar_palavra(id,palavra,dificuldade,qtdTentativas,(qtdJogadas+1),(qtdAcertos+1))
                    break
                else:
                    print('\n\nVocê falhou! \n a palavra era: ' + palavra)
                    input('\n>>> Pressione para sair desta Tela <<<')
                    GDB.retornar_palavra(id,palavra,dificuldade,qtdTentativas,(qtdJogadas+1),qtdAcertos)
                    break
            tentativas += 1
        elif userChoice == '2':
            userPalavra = input('Qual palavra deseja tentar? ')
            #Verificação se a palavra está correta
            if userPalavra.upper() == palavra:
                print('\n\nParabéns você ganhou!!!\n a palavra é:' + palavra)
                input('\n>>> Pressione para sair desta Tela <<<')
                GDB.retornar_palavra(id,palavra,dificuldade,qtdTentativas,(qtdJogadas+1),(qtdAcertos+1))
                break
            else:
                print('\n\nVocê falhou! \n a palavra era: ' + palavra)
                input('\n>>> Pressione para sair desta Tela <<<')
                GDB.retornar_palavra(id,palavra,dificuldade,qtdTentativas,(qtdJogadas+1),qtdAcertos)
                break
        
    
        
        
        