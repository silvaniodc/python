# -*- coding: UTF-8 -*-

import re

def cadastrar(nomes):

	sair = '2'

	while (sair != '0') :
		print 'Digite o nome desejado ou 0 para sair:'
		nome = raw_input()

		if nome != '0' :
			nomes.append(nome)
		else :
			sair = '0'	

def listar(nomes):

	print 'Lista de nomes:'
	for nome in nomes:
		print nome

def procurar_regex(nomes):

	print('Digite a expressão regular.')

	regex = raw_input()
   
	nomes_concat = ' '.join(nomes)

	print regex
	print nomes_concat
	
	resultado = re.findall(regex , nomes_concat)
	print(resultado)


def remover(nomes):
	print 'Digite o nome a ser removido:'
	nome = raw_input()

	if nome in nomes :
		nomes.remove(nome)
	else:
		print 'O nome digitado não foi encontrado'


def alterar(nomes):
	print 'Qual nome deseja alterar:'
	nome = raw_input()

	if nome in nomes :
		print 'Digite novo nome:'
		novo_nome = raw_input()
		nomes [nomes.index(nome)] = novo_nome
		listar(nomes)
	else:
		print 'O nome digitado não foi encontrado'

def procurar(nomes):

	print 'Digite o nome a ser encontrado:'
	nome = raw_input()

	if nome in nomes:
		posicao = nomes.index(nome)
		print 'O nome %s foi encontrado na posição %s da lista.' % (nome, posicao)
	else:
		print 'ERRO - O nome %s não foi encontrado na lista.' % (nome)	

def menu():

	nomes = []
	escolha = ' '

	while(escolha != '0'):

		print 'Digite : 1 Cadastrar, 2 Listar, 3 Remover, 4 Alterar, 5 Procurar, 6 Expressoes e 0 para sair:'
		escolha = raw_input()

		if escolha == '1' :
			cadastrar(nomes)
		if escolha == '2' :
			listar(nomes)
		if escolha == '3' :
			remover(nomes)
		if escolha == '4' :
			alterar(nomes)
		if escolha == '5' :
			procurar(nomes)
		if escolha == '6' :
			procurar_regex(nomes)


menu()