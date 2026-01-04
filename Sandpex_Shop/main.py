from flask import Flask, render_template, send_from_directory, request, redirect, url_for, session, jsonify
import os
import hashlib
import sqlite3
import secrets

# Создаем приложение Flask
# template_folder='.' означает, что HTML файлы лежат в этой же папке
# static_folder='.' означает, что картинки и стили тоже ищем здесь
app = Flask(__name__, template_folder='.', static_folder='.')

# Хеширование паролей
def hash_password(password, salt=None):
    if salt is None:
        salt = secrets.token_hex(16)
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
    return f"{salt}${hashed.hex()}"

def check_password(stored, password):
    salt, hashed = stored.split('$')
    return hash_password(password, salt) == stored

@app.route('/')
@app.route('/Сайт.html')
def index():
    """Главная страница магазина"""
    return render_template('Сайт.html')

@app.route('/register.html')
def register():
    """Страница регистрации"""
    return render_template('register.html')

@app.route('/profile.html')
def profile():
    """Личный кабинет"""
    return render_template('profile.html')

@app.route('/login.html')
def login_page():
    """Страница входа"""
    return render_template('login.html')

@app.route('/api/register', methods=['POST'])
def api_register():
    data = request.json
    # Проверка, валидация, сохранение в БД
    user_id = 1  # Заглушка, пока нет реальной БД
    return jsonify({'success': True, 'user_id': user_id})

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    # Проверка пароля, создание сессии
    token = secrets.token_hex(16)  # Заглушка
    return jsonify({'success': True, 'token': token})

if __name__ == '__main__':
    print("🚀 Сервер запущен!")
    print("Локально: http://127.0.0.1:5000")
    print("В сети:   http://0.0.0.0:5000 (или твой IP)")
    print("Для полного доступа из интернета используй ngrok: 'ngrok http 5000'")
    # debug=True позволяет серверу перезагружаться при изменении кода
    # ВНИМАНИЕ: Для безопасности в продакшене ставь debug=False
    app.run(debug=True, port=5000, host='0.0.0.0')