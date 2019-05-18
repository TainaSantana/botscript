import json

from flask import Flask, request

from bot import Bot

PAGE_ACCESS_TOKEN = 'EAAGVUSkAlM4BAJnqJqWeCto9MSdX8tiCXH3b7lvtKFD5Md00ThV5Pv7NbsjDgTKRv9xCpZAlXdYx6ZClb7IZAXwmLV3sJJEXwZBVGWD5Fws6m2TpuRx2e766GvS1XtXmsENZA5Pd0G3IvZCOfh5j5GNeMzjezX0vqpUsWdZCY4TcV4WeUt67Vgz'
GREETINGS = ['oi', 'ola', 'ei', 'hello']

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def webhook():
     if request.method == 'GET':
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == 'secret':
            return str(challenge)
        return '400'

     else:
	data = json.loads(request.data)
	messaging_events = data['entry'][0]['messaging']
	bot = Bot(PAGE_ACCESS_TOKEN)
	for message in messaging_events:
		user_id = message['sender']['id']
		text_input = message['message'].get('text')
		response_text = 'Ola, eu nao entendi.Ainda estou aprendendo'
		if text_input in GREETINGS:
			response_text = 'Ola eu sou o bot Luisa'
		#print('Mensagem do usuario de ID {} - {}'.format(user_id, text_input))
		bot.send_text_message(user_id, response_text)
        return '200'


if __name__ == '__main__':
    app.run(debug=True)
