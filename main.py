#!/usr/bin/env python
#encoding: UTF-8
import os
import gerenciadorDB as GDB
import forca as F
import string

def gerenciadorDB():
    '''
    Função Menu para Gerenciar o Banco de Dados
    '''
    while True:
        print('Escolha uma opção:\n1 - Adicionar uma Palavra;\n2 - Remover uma palavra;\n3 - Consultar todos os dados de uma palavra;\n4 - Listar todas as palavras cadastradas;')
        print('5 - Buscar as palavras a partir de uma fração da palavra;\n6 - Listar todas as palavras de uma dificuldade;\n7 - Apresentar estatísticas;\n8 - Voltar ao Menu Inicial.')
        userChoice = (int)(input('Selecione uma Opção: '))
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if userChoice == 1:
            palavra = input('Qual a palavra que deseja Adicionar: ').upper()
            dificuldade = (int)(input('Qual a dificuldade da palavra(1 - para fácil, 2 - para médio, 3 - para difícil): '))
            GDB.adicionar_Palavra((GDB.ultimoID()+1),palavra,dificuldade,6,0,0)
            print('\n\n Palavra Adicionada!')
            input('\n>>> Pressione para Voltar ao Menu <<<')
            os.system('cls' if os.name == 'nt' else 'clear')
        elif userChoice == 2:
            palavra = input('Qual a palavra que deseja Remover: ').upper()
            GDB.remover_Palavra(palavra)
            print('\n\n Palavra Removida!')
            input('\n>>> Pressione para Voltar ao Menu <<<')
            os.system('cls' if os.name == 'nt' else 'clear')
        elif userChoice == 3:
            palavra = input('Qual a palavra que deseja Consultar: ').upper()
            os.system('cls' if os.name == 'nt' else 'clear')
            GDB.consultar(palavra)
            input('\n>>> Pressione para voltar ao Menu <<<')
            os.system('cls' if os.name == 'nt' else 'clear')
        elif userChoice == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            GDB.listar()
            input('\n>>> Pressione para voltar ao Menu <<<')
            os.system('cls' if os.name == 'nt' else 'clear')
        elif userChoice == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            palavra = input('Qual a parte da palavra que quer procurar: ').upper()
            print('\n')
            GDB.buscar(palavra)
            input('\n>>> Pressione para voltar ao Menu <<<')
            os.system('cls' if os.name == 'nt' else 'clear')
        elif userChoice == 6:
            dificuldade = (int)(input('Qual a dificuldade deseja pesquisar(1 - para fácil, 2 - para médio, 3 - para difícil): '))
            os.system('cls' if os.name == 'nt' else 'clear')
            GDB.listar_dificuldade(dificuldade)
            input('\n>>> Pressione para voltar ao Menu <<<')
            os.system('cls' if os.name == 'nt' else 'clear')
        elif userChoice == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            GDB.apresentar_estatísticas()
            input('\n>>> Pressione para voltar ao Menu <<<')
            os.system('cls' if os.name == 'nt' else 'clear')
        elif userChoice == 8:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print('Escolha Uma das opções acima!')

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Escolha uma opção:')
        print('1 - Para Jogar a Forca;\n2 - Para Entrar no modo Gerenciador;\n3 - Para Sair do jogo')
        userChoice = input('Sua Opção: ')
        
        if userChoice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            F.jogo()
        elif userChoice == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            gerenciadorDB()
        elif userChoice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print('\n Escolha Uma das Opções Acima!!!')
            
            
if (__name__ == "__main__"):
    main()
