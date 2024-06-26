from flask import Flask, request, jsonify
from flask_cors import CORS
import ssl

app = Flask(__name__)
CORS(app)

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = float(num1) + float(num2)
    return jsonify({'result': result})

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.load_cert_chain('cert.pem', 'key.pem')
    app.run(debug=True, host='0.0.0.0', port=5000, ssl_context=context)
