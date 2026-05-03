from flask import Flask, request

app = Flask(__name__)

# Читаем HTML-файлы
with open('templates/index.html', 'r', encoding='utf-8') as f:
    HTML_INDEX = f.read()

with open('templates/contacts.html', 'r', encoding='utf-8') as f:
    HTML_CONTACTS = f.read()

@app.route('/')
def index():
    return HTML_INDEX, 200, {'Content-Type': 'text/html'}

@app.route('/contacts', methods=['GET'])
def contacts_page():
    return HTML_CONTACTS, 200, {'Content-Type': 'text/html'}

@app.route('/contacts', methods=['POST'])
def handle_contact():
    print("=== НОВОЕ СООБЩЕНИЕ ===")
    print(f"Имя: {request.form.get('name')}")
    print(f"Email: {request.form.get('email')}")
    print(f"Сообщение: {request.form.get('message')}")
    print("==========================")
    return "Сообщение отправлено. Спасибо!", 200

@app.errorhandler(404)
def not_found(e):
    return "<h1>404</h1><p>Страница не найдена</p>", 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
