# -*- coding: utf-8 -*-
#Não á conexão real, apenas material para o aprendizado sobre Patterns Factory

import MySQLdb

class Connection_factory(object):		

	def get_connection(self):
	 	
		connection=MySQLdb.connect(
			host='localhost',
			user='root',
			passwd='',
			db='alura')

		return connection