
# -*- coding: UTF-8 -*-

from impostos import ISS, ICMS, IKCV, ICPP

class Calculador_de_impostos(object):

	def realiza_calculo(self, orcamento, imposto):
		
		valor = imposto.calcula(orcamento)
		print valor

if __name__ == '__main__':

	from orcamento import Orcamento, Item
	from impostos import ISS, ICMS, IKCV, ICPP

	calculador = Calculador_de_impostos()
	orcamento = Orcamento()

	orcamento.adiciona_item(Item('ITEM 1', 50))
	orcamento.adiciona_item(Item('ITEM 1', 200))
	orcamento.adiciona_item(Item('ITEM 1', 250))		

	print 'INSS e ICMS'
	calculador.realiza_calculo(orcamento, ISS())
	calculador.realiza_calculo(orcamento, ICMS())
	print 'INSS com ICMS'
	calculador.realiza_calculo(orcamento, ISS(ICMS()))

	print 'ICPP e IKCV'
	calculador.realiza_calculo(orcamento, ICPP())
	calculador.realiza_calculo(orcamento, IKCV())
	print 'ICPP com IKCV'
	calculador.realiza_calculo(orcamento, ICPP(IKCV()))
	