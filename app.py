# Importing essentials

from flask import Flask, request
from pymessenger.bot import Bot
import os
from engine import jarvis

# Definitions

bot = Bot(os.environ['FB_ACCESS_TOKEN'])
app = Flask(__name__)
VERIFY_TOKEN = "a"
update_id = None

def craft_message(user_id, msg):
    for x in msg:
        if type(x) is list:
            bot.send_generic_message(user_id, x)
        else:
            bot.send_text_message(user_id, x)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        else:
            return "Invalid verification token"

    if request.method == 'POST':
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for x in messaging:
                if x.get('message'):
                    if x['message'].get('text'):
                        # Logging - print x
                        craft_message(x['sender']['id'], jarvis.do(x['message']['text']))
                else:
                    pass
        return "Success"

# Booting server

if __name__ == '__main__':
    app.run()
