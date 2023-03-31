
from flask import Flask, abort, request

server = Flask(__name__)


# webhook_url = 'http://127.0.0.1:5000/webhook'
# webhook_url = 'https://webhook.site/5704e368-734e-4354-ba5d-dc09948e2496'

data = {'name': 'Message for success'}

# requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

@server.route('/webhook', methods=['POST'])
def get_webhook():
    if request.method == 'POST':
        print("received data: ", request.json)
        return 'success', 200
    else:
        abort(400)



if __name__ == '__main__':
    server.run()