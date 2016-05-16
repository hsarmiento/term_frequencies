#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb

#config db
DB = MySQLdb.connect(
	host="", # your host, usually localhost
	user="", # your username
	passwd="", # your password
	db=""  # name of the data base
	) 

#queries
COUNT = ""  #query for total rows
QUERY = ""   #your query. Include limit and offset for batch size


#CONSTANT VARIABLES
BATCH_SIZE = 250000  #set batch size