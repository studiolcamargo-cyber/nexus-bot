from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    dados = request.get_json()
    # Pega o número de quem te chamou
    numero = dados.get('sender') or dados.get('phone')
    
    if numero:
        url = "https://api.z-api.io/instances/3ED56F6CCFB82334751CB6C5C732398F/token/948A09A8C22A436CAE0CD4C8/send-text"
        payload = {"phone": numero, "message": "NEXUS: Recebi seu sinal! 🦾"}
        
        # Envia e captura a resposta da Z-API
        resposta = requests.post(url, json=payload)
        
        # ISSO AQUI VAI NOS DIZER O ERRO NO RENDER:
        print(f"Tentativa para {numero} | Status: {resposta.status_code} | Resposta: {resposta.text}")
    
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
