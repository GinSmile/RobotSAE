# -*- coding: utf-8 -*-
from flask import Flask, render_template
import os
import json
import urllib2
import urllib
import time
import sys;
from tools import myToken
from tools import greet

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/chime', methods=['GET', 'POST'])
def chime():
	hour = time.strftime('%H',time.localtime(time.time()))

	#每次发微博重新授权
	token = myToken.getToken();
	content = "" + greet.duang(hour) + greet.morning(hour);
	data = {'access_token':token,'status':content}
	data_urlencode = urllib.urlencode(data)
	requrl = "https://api.weibo.com/2/statuses/update.json"
	req = urllib2.Request(url = requrl,data =data_urlencode)
	urllib2.urlopen(req,timeout=60)
	return 'send success!'


  
if __name__ == '__main__':
		app.run()
