from flask import Flask, request
import requests

app = Flask(__name__)

DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/your_webhook_id/your_webhook_token'

@app.route('/log_ip', methods=['POST'])
def log_ip():
    data = request.json
    ip = data.get('ip')
    if ip:
        payload = {
            'content': f'IP Address: {ip}'
        }
        requests.post(DISCORD_WEBHOOK_URL, json=payload)
        return 'IP logged', 200
    return 'No IP found', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
