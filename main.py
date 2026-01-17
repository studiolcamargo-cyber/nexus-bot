from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "NEXUS ONLINE NO RENDER 🚀"

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        dados = request.get_json()
        numero = dados.get('phone')
        # URL da sua Z-API (conforme Foto c56494fe)
        url = "https://api.z-api.io/instances/3ED56F6CCFBB2334751CB6C5C732398F/token/948A09A8C22A436CAE0CD4C8/send-text"
        payload = {"phone": numero, "message": "NEXUS ATIVADO PELO RENDER! 🦾"}
        requests.post(url, json=payload)
        return "OK", 200
    except:
        return "Erro", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
