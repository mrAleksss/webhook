import requests
import json


webhook_url = 'http://127.0.0.1:5000/webhook'
# webhook_url = 'https://webhook.site/5704e368-734e-4354-ba5d-dc09948e2496'
data = {'name': 'Message for success'}


requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})