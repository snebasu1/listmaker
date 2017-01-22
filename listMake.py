import datetime 
import os

from collections import OrderedDict 
from peewee import *

db = #arbitrary database
class listName(model):
 #model for the to do list that allows for protection and deleting done items. 
	task = CharField(max_length = 220)
	timeMarker = DateTimeField(default = datetime.datetime.now)
	done = booleanField(default = false)
	protected = booleanField(default = true)
	
	class Meta:
		database = db

#define a function to cross off lists
def closeFunction
