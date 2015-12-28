# TelegramBotPythonAppEngine
A easy way to manage a Telegram Bot in App Engine


First of all set your bot:

bot = TelegramBot()
bot.token = [your token as a string]

Then set your Web Hook (where Telegram will post the received chat messages).
bot.setWebHooK([your url])

In App Engine create the class to manage the Web Hook:
class WebHookHandler(webapp2.RequestHandler):
	def post(self):
		bot.WebHook(self.request.body)
		
Then you will have the messagge and some vars to use it:
bot.command : True if the messagge is a command)
bot.testout : The text of the messagge)
bot.chat_id : The Telegram id of the chat

To send a message:
Set the bot.testomsg and use bot.sendMessage() to send it.
If you are an answering to a chat the bot.chat_id is just setted, otherwise set it.

