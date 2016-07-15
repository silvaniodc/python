# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod

class Estado_de_um_orcamento(object):
	__metaclass__ = ABCMeta

	def __init__(self):
		self.desconto_aplicado = False

	@abstractmethod
	def aplica_desconto_extra(self, orcamento):
		pass

	@abstractmethod
	def aprova(self, orcamento):
		pass
	
	@abstractmethod
	def reprova(self, orcamento):
		pass

	@abstractmethod
	def finaliza(self, orcamento):
		pass

class Em_aprovacao(Estado_de_um_orcamento):
	
	def aplica_desconto_extra(self, orcamento):
		
		if(not self.desconto_aplicado):
			orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)
			self.desconto_aplicado = True
		else:
			raise Exception('Desconto já Aplicado.')

	def aprova(self, orcamento):
		orcamento.estado_atual = Aprovado()

	def reprova(self, orcamento):
		orcamento.estado_atual = Reprovado()

	def finaliza(self, orcamento):
		raise Exception('Orçamento em aprovação não podem ir para finalizado.')
		
class Aprovado(Estado_de_um_orcamento):
	
	def aplica_desconto_extra(self, orcamento):
		
		if (not desconto_aplicado)
			orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)
			self.desconto_aplicado = True
		else:
			raise Exception('Desconto já Aplicado.')

	def aprova(self, orcamento):
		raise Exception('Orçamento já está aprovado.')

	def reprova(self, orcamento):
		raise Exception('Orçamentos aprovados não podem ser reprovados.')

	def finaliza(self, orcamento):
		orcamento.estado_atual = finaliza()

class Reprovado(Estado_de_um_orcamento):
	
	def aplica_desconto_extra(self, orcamento):
		raise Exception('Orçamentos reprovados não receberam desconto extra.')

	def aprova(self, orcamento):
		raise Exception('Orçamento reprovado não pode ser aprovado.')

	def reprova(self, orcamento):
		raise Exception('Orçamentos reprovados não podem ser reprovados novamente.')

	def finaliza(self, orcamento):
		orcamento.estado_atual = finalizado()

class finaliza(Estado_de_um_orcamento):
		
	def aplica_desconto_extra(self, orcamento):
		raise Exception('Orçamentos finalizados não receberam desconto extra.')

	def aprova(self, orcamento):
		raise Exception('Orçamentos finalizados não podem ser aprovado.')

	def reprova(self, orcamento):
		raise Exception('Orçamentos finalizados não podem ser reprovados.')

	def finaliza(self, orcamento):
		raise Exception('Orçamentos finalizados não podem ser finalizados novamente.')

class Orcamento(object):

	#Construtor da Classe instancia uma lista de Itens
	def __init__(self):
		self.__itens = []
		self.estado_atual = Em_aprovacao()
		self.__desconto_extra = 0

	def aprova(self):
		self.estado_atual.aprova(orcamento)

	def reprova(self):
		self.estado_atual.reprova(orcamento)

	def finaliza(self):
		self.estado_atual.finaliza(orcamento)

	def aplica_desconto_extra(self):
		self.estado_atual.aplica_desconto_extra(self)

	def adiciona_desconto_extra(self, desconto):
		self.__desconto_extra += desconto

	#Somas os itens e retorna o total do orçamento.
	@property	
	def valor(self):

		total = 0.0

		for item in self.__itens:
			total += item.valor

		return total - self.__desconto_extra

	#Retorna uma Tupla...?
	def obter_itens(self):
		return tuple(self.__itens)

	#Pergunta ao Orçamento o total de Itens
	@property
	def total_itens(self):
		return len(self.__itens)		

	#Adiciona mais itens ao Orcamento
	def adiciona_item(self, item):
		self.__itens.append(item)


class Item(object):
	
	#Construtor da Classe instanciando os atributos do Item
	def __init__(self, nome, valor):
		self.__nome = nome
		self.__valor = valor

	#Retorna o Valor do item
	@property
	def valor(self):
		return self.__valor

	#Retorna o nome do Item
	@property
	def nome(self):
		return self.__nome

if __name__ == '__main__':

	orcamento = Orcamento()

	orcamento.adiciona_item(Item('ITEM 1', 100))
	orcamento.adiciona_item(Item('ITEM 1', 50))
	orcamento.adiciona_item(Item('ITEM 1', 400))

	print orcamento.valor
	
	orcamento.aprova()
	orcamento.reprova()
			

	
	

	
		