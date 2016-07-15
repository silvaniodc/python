# -*- coding: UTF-8 -*-

# O que Silvanio vai fazer no Domingo?

def hoje_e_o_dia():
	
	from datetime import date
	hj = date.today()

	dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')

	dia = int(hj.weekday())

	if dia == 3 :
		print 'Hoje é %s e Silvânio vai continuar Estudando insanamente...!' % (dias[hj.weekday()])

	if dia == 1 :
		print 'Hoje é %s e Silvânio vai na Ubercom ver se o HD SSD ja chegou!' % (dias[hj.weekday()])

	if dia == 6 :
		print 'Hoje é %s e com certeza Silvânio vai pescar :) ' % (dias[hj.weekday()])

	if dia == 5 :
		print 'Hoje é %s e Silvânio vai levar Janaina pra tomar Açai!' % (dias[hj.weekday()])

	if dia == 2 :
		print 'Hoje é %s e Silvânio vai estudar Inglês igual um a louco!' % (dias[hj.weekday()])

	if dia == 0 :
		print 'Hoje é %s e Silvânio vai faze um Churrasco de Picanha au au!' % (dias[hj.weekday()])

	if dia == 4 :
		print 'Hoje é %s e Silvânio vai assistir Family Guy na Netflix!' % (dias[hj.weekday()])

hoje_e_o_dia()	