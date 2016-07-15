# -*- coding: utf-8 -*-
#Não á conexão real, apenas material para o aprendizado sobre Patterns Factory

import MySQLdb
from connection_factory import Connection_factory

connection = Connection_factory().get_connection()

cursor = connection.cursor()

cursor.execute('SELECT * FROM cursor')

for linha in cursor:
	print linha

connection.close()