# -*- coding: UTF-8 -*-

class Perfil(object):

	def __init__(self, nome, telefone, empresa):
		if(len(nome) < 3):
			raise ArgumentoInvalidoErro('Nome deve ter pelo menos 3 caracteres.')
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0
		

	def curtir(self):
		self.__curtidas += 1

	def obter(self):		
		return self.__curtidas

	@classmethod
	def gerar_perfil(classe, nome_arquivo):
		arquivo = open(nome_arquivo,'r')
		perfis = []

		for linha in arquivo:
			valores = linha.split(',')
			
			if(len(valores) is not 3):
				raise ValueError('Uma linha no arquivo %s deve ter 3 valores' % nome_arquivo)
			
			perfis.append(classe(*valores))

		arquivo.close()
		return perfis

	def imprimir(self):
		print 'Nome : %s, Telefone: %s, Empresa: %s' % (self.nome, self.telefone, self.empresa)


class Perfil_vip(Perfil):

	def __init__(self, nome, telefone, empresa, apelido=''):
		super(Perfil_vip, self).__init__(nome, telefone, empresa)
		self.apelido = apelido
	
	def creditos(self):
		return super(Perfil_vip, self).obter() * 10.0

class ArgumentoInvalidoErro(Exception):
	def __init__(self, mensagem):
		self.mensagem = mensagem

	def __str__(self):
		return repr(self.mensagem)
		
	
class Data(object):
			
	def __init__(self, d, m, a):				
		self.d = d
		self.m = m
		self.a = a

	def imprime(self):
		print 'A data é: %s/%s/%s' % (self.d, self.m, self.a)

class Pessoa(object):
			
	def __init__(self, nome, peso, altura):				
		self.nome = nome
		self.peso = peso
		self.altura = altura

	def imprime(self):
				
		print 'Imc de %s: %s' % (self.nome, self.peso / (self.altura **2))	
						

		