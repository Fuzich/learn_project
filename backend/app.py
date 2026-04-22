from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    """главная страница апи"""
    return jsonify({
        'message': 'API Системы учета товаров',
        'version': '1.0.0',
        'endpoints': {
            'GET /': 'Информация об API',
            'GET /health': 'Проверка состояния сервера'
        }
    })

@app.route('/health')
def health_check():
    """проверка работоспособности сервера"""
    return jsonify({'status': 'ok'}), 200
if __name__ == '__main__':
