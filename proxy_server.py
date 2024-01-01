from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

DISCORD_API_URL = "https://discord.com/api/v10"

@app.route('/get_user_info/<user_id>', methods=['GET'])
def get_user_info(user_id):
    token = os.environ.get('MTE5MTM1MTYwODM3NDczNDkxOA.GEIY3J.jeYOiskPR4x8n1YokDhK-hzDrLD0-MD2bFyTRg')
    headers = {'Authorization': f'Bot {token}'}
    
    response = requests.get(f"{DISCORD_API_URL}/users/{user_id}", headers=headers)
    data = response.json()
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
