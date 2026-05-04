from flask import Flask, request

app = Flask(__name__)

# Читаем все HTML-файлы
with open('templates/index.html', 'r', encoding='utf-8') as f:
    HTML_INDEX = f.read()

with open('templates/catalog.html', 'r', encoding='utf-8') as f:
    HTML_CATALOG = f.read()

with open('templates/category.html', 'r', encoding='utf-8') as f:
    HTML_CATEGORY = f.read()

with open('templates/contacts.html', 'r', encoding='utf-8') as f:
    HTML_CONTACTS = f.read()

with open('templates/orders.html', 'r', encoding='utf-8') as f:
    HTML_ORDERS = f.read()

@app.route('/')
def index():
    return HTML_INDEX, 200, {'Content-Type': 'text/html'}

@app.route('/catalog')
def catalog():
    return HTML_CATALOG, 200, {'Content-Type': 'text/html'}

@app.route('/category')
def category():
    return HTML_CATEGORY, 200, {'Content-Type': 'text/html'}

@app.route('/orders')
def orders():
    return HTML_ORDERS, 200, {'Content-Type': 'text/html'}

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
