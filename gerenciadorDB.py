#!/usr/bin/env python
#encoding: UTF-8

import csv
import pandas as pd
import random

def adicionar_Palavra(id, palavra, dificul, qtd_tent, qtd_jog, qtd_acertos):
    '''
    Função para adicionar uma palavra do arquivo CSV
    '''
    if verificar(palavra):
        with open(filename, 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile,delimiter=';',quoting=csv.QUOTE_MINIMAL)
            csvwriter.writerow([id,palavra,dificul,qtd_tent,qtd_jog,qtd_acertos])
    else:
        print('\n palavra ja existe no banco de dados!!! \n\n')


def remover_Palavra(palavra):
    '''
    Função para remover uma palavra do arquivo CSV
    '''
    if verificar(palavra):
        print('\nPalavra não existe no banco de dados!!! \n\n')
    else:
        df = pd.read_csv(filename,delimiter=';')
        df = df[df.palavra != palavra]
        df.to_csv(filename,index=False,sep=';')
     
 
def verificar(palavra):
    '''
    Função interna para verificar se uma palavra está na ou não no arquivo csv
    '''
    df = pd.read_csv(filename, sep=';')
    df = df[(df['palavra'] == palavra)]
    if df.empty:  #retorna verdadeiro se o dataframe estiver vazio, o que significa que ele não achou a palavra
        return True
    else:
        return False
    
def consultar(palavra):
    '''
    Função para consultar todos os dados de uma palavra no arquivo csv
    '''
    if verificar(palavra):
        print('\nPalavra não existe no banco de dados!!! \n\n')
    else:
        df = pd.read_csv(filename, sep=';')
        df = df[(df['palavra'] == palavra)]
        print(df.to_string(index=False))
        
    
def listar():
    '''
    Função para listar todos as palavras cadastradas no arquivo csv
    '''
    df = pd.read_csv(filename,sep=';')
    print(df.to_string(index=False))
     
     
def buscar(palavra):
    '''
    função para mostrar todas as palavras a partir de uma parte da palavra
    '''
    df = pd.read_csv(filename, sep=';')
    df = df[df['palavra'].str.contains(palavra, na = False)]
    if df.empty:
        print('\nNão existe palavra com esses caracteres!!!\n\n')
    else:
        print(df.to_string(index=False))

    
def listar_dificuldade(dificuldade):
    '''
    Função para listar todas as palavras de uma determinada dificuldade
    '''
    df = pd.read_csv(filename, sep=';')
    df = df[df['dificuldade'] == dificuldade]
    if df.empty:
        print('\nNão existe palavra para esta dificuldade!!!\n\n')
    else:
        print(df.to_string(index=False))

def apresentar_estatísticas():
    '''
    Função para apresentar as 5 palavras mais jogadas, 5 com mais acertos, 5 com mais erros
    '''
    df = pd.read_csv(filename, sep=';')
    dfl = df.nlargest(5,'qtd_jogadas')[['id','palavra','qtd_jogadas']]
    print(dfl.to_string(index=False))
    print('\n')
    dfl = df.nlargest(5,'qtd_de_acertos')[['id','palavra','qtd_de_acertos']]
    print(dfl.to_string(index=False))
    print('\n')
    #Seção para criação da coluna erros
    df['qtd_erros'] = df['qtd_jogadas'] - df['qtd_de_acertos']
    dfl = df.nlargest(5,'qtd_erros')[['id','palavra','qtd_erros']]
    print(dfl.to_string(index=False))
    print('\n')
    
def escolher_palavra(dificuldade):
    '''
    Função para retornar uma palavra de acordo com a dificuldade
    '''
    palavra_escolhida = []
    df = pd.read_csv(filename,sep=';')
    df = df[df['dificuldade'] == dificuldade]
    if df.empty:
        print('\nNão existe palavra para esta dificuldade!!!\n\n')
    else:
        listaindex = (df.index.values) #cria uma lista com os Id's das palavras da dificuldade desejada
        x = random.randrange(0,len(listaindex))  #randomiza um indice da lista de index
        palavra_escolhida.append(df['id'].loc[listaindex[x]])
        palavra_escolhida.append(df['palavra'].loc[listaindex[x]])
        palavra_escolhida.append(df['dificuldade'].loc[listaindex[x]])
        palavra_escolhida.append(df['qtd_de_tentativas'].loc[listaindex[x]])
        palavra_escolhida.append(df['qtd_jogadas'].loc[listaindex[x]])
        palavra_escolhida.append(df['qtd_de_acertos'].loc[listaindex[x]])
    
    return(palavra_escolhida)


def retornar_palavra(id,palavra,dificuldade,qtd_tent,qtd_jogadas,qtd_acertos):
    '''
    Função para retornar a palavra com as devidas modificações para o arquivo CSV
    '''
    df = pd.read_csv(filename,sep=';')
    df.loc[(id-1):(id-1)] = id, palavra, dificuldade, qtd_tent, qtd_jogadas, qtd_acertos
    df.to_csv(filename,index=False,sep=';')
    
def ultimoID():
    '''
    Retorna o Último Id que foi adicionado
    '''
    df = pd.read_csv(filename,sep=';')
    dfl = df.nlargest(1,'id')[['id']]
    ultimoIndice = dfl['id'].squeeze()
    return(ultimoIndice)
    
filename = 'database.csv'




