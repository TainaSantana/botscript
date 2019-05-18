import requests
import json

FACEBOOK_GRAPH_URL = 'https://graph.facebook.com/v3.3/me/'

class Bot(object):
	def __init__(self, access_token, api_url=FACEBOOK_GRAPH_URL):
		self.access_token = access_token
		self.api_url = api_url

	def send_text_message(self, psid, message, messaging_type="RESPONSE"):
		headers = {
			'Content-Type': 'application/json'
		}

		data = {
			'messaging_type': messaging_type,
			'recipient': {'id': psid},
			'message': {'text': message}
		}

		params = {'access_token': self.access_token}
		self.api_url = self.api_url + 'messages'
		response = requests.post(self.api_url,
					headers=headers, params=params,
					data=json.dumps(data))
		print(response.content)

bot = Bot('EAAGVUSkAlM4BAJnqJqWeCto9MSdX8tiCXH3b7lvtKFD5Md00ThV5Pv7NbsjDgTKRv9xCpZAlXdYx6ZClb7IZAXwmLV3sJJEXwZBVGWD5Fws6m2TpuRx2e766GvS1XtXmsENZA5Pd0G3IvZCOfh5j5GNeMzjezX0vqpUsWdZCY4TcV4WeUt67Vgz')
#bot.send_text_message(2144930868917883, 'ola')
#bot.send_text_message(user_id, 'ola')
