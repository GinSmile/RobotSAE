# -*- coding: utf-8 -*-
import random
import urllib2
import json
import re
import string

#发duang函数
def duang(hour):
	lines = [
	'duang duang duang duang duang duang duang duang duang duang duang duang～',
	'duang～',
	'duang duang～',
	'duang duang duang～',
	'duang duang duang duang～',
	'duang duang duang duang duang～',
	'duang duang duang duang duang duang～',
	'duang duang duang duang duang duang duang～',
	'duang duang duang duang duang duang duang duang～',
	'duang duang duang duang duang duang duang duang duang～',
	'duang duang duang duang duang duang duang duang duang duang～',
	'duang duang duang duang duang duang duang duang duang duang duang ～'
	]
	
	index = (int)(string.atof(hour)) % 12
	return lines[index]

def morning(hour):
	if hour == 22:
		return " 晚安，东大～"
	if hour == 6:
		return " 早安，东大～"
	return ""