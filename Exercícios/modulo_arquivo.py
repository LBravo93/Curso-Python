
from modulo_cores import *


def verificExisteArquivo(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except(FileNotFoundError):
        return False
    else:
        return True


def criartxt(nome):
    try:
        with open(nome, "w") as arquivo:
            print(amarelo(f'Arquivo de registro foi criado com sucesso.'))
    except FileNotFoundError:
        print(vermelho('Houve um erro na criação do arquivo'))
    finally:
        arquivo.close()


def mostrartxt(arq):
    try:
        arquivo = open(arq, 'r')
        for valor in arquivo:
            dado = valor.split(';')
            print(verde(f'{dado[0]:<30}{dado[1]:<5} anos'.replace('\n', '')))
    except:
        print(vermelho('Houve um erro!! Tente novamente'))

    finally:
        arquivo.close()


def adicionartxt(arq, nome='Desconhecido', idade=0,):
    try:
        arquivo = open(arq, 'a')
    except:
        print(vermelho('Houve um erro! Tente novamente.'))
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print(vermelho('Houve um erro! Tente novamente.'))
        else:
            print(f'Novo registro "{nome}" Adicionado.')
            arquivo.close()
