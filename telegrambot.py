from __future__ import unicode_literals
import urllib
import json
import sys
from google.appengine.api import urlfetch


reload(sys)
sys.setdefaultencoding('utf-8')

class TelegramBot():
	def __init__(self):
		self.testomsg = ''
		self.token = ''
		self.ListeTastiera = []
		self.chat_id = ''
		self.testout = ''
		self.user = ''
		self.first_name = ''
		self.url = ''
		self.command = False


	#Invio Messaggio con Tastiera
	def sendMessageKeyBoard(self):
		reply_markup = json.dumps({'keyboard':self.ListeTastiera})
		form_fields = {'chat_id': self.chat_id, 'text': self.testomsg, 'reply_markup':reply_markup}
		self.url = 'https://api.telegram.org/bot%s/sendMessage' % self.token
		form_data = urllib.urlencode(form_fields)
		result = urlfetch.fetch(url=self.url,
		    payload=form_data,
		    method=urlfetch.POST,
		    headers={'Content-Type': 'application/x-www-form-urlencoded'})
		return result

	def sendMessageHideKeyBoard(self):
		reply_markup = json.dumps({'hide_keyboard':'True'})
		form_fields = {'chat_id': self.chat_id, 'text': self.testomsg, 'reply_markup':reply_markup}
		self.url = 'https://api.telegram.org/bot%s/sendMessage' % self.token
		form_data = urllib.urlencode(form_fields)
		result = urlfetch.fetch(url=self.url,
		    payload=form_data,
		    method=urlfetch.POST,
		    headers={'Content-Type': 'application/x-www-form-urlencoded'})
		return result


	#Invio Messaggio Semplice
	def sendMessage(self):
		form_fields = {'chat_id': self.chat_id, 'text': self.testomsg}
		self.url = 'https://api.telegram.org/bot%s/sendMessage' % self.token
		form_data = urllib.urlencode(form_fields)
		result = urlfetch.fetch(url=self.url,
		    payload=form_data,
		    method=urlfetch.POST,
		    headers={'Content-Type': 'application/x-www-form-urlencoded'})
		return result

	#Gestione WebHook
	def WebHook(self, testoinput):
		tgmsg = json.loads(testoinput)
		self.chat_id = tgmsg["message"]["chat"]["id"]
		try:
			self.testout = tgmsg["message"]["text"]
		except:
			self.testout = 'vuoto'
		self.user = tgmsg["message"]["from"]["id"]
		self.first_name = tgmsg["message"]["from"]["first_name"]
		if self.testout[0:1] == '/':
			self.command = True
		return 'ok'

	#Invio url gestione WebHook
	def setWebHooK(self, urlarrivo):
		form_fields = {'url': urlarrivo}
		urlWH = 'https://api.telegram.org/bot%s/setWebhook' % self.token
		form_data = urllib.urlencode(form_fields)
		result = urlfetch.fetch(url=urlWH,
		    payload=form_data,
		    method=urlfetch.POST,
		    headers={'Content-Type': 'application/x-www-form-urlencoded'})
		return result
