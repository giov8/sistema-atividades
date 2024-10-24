from flask import Flask, render_template, request
app = Flask(__name__)

# Dados de exemplo (normalmente, isso estaria em um banco de dados)
users = {
    'admin': 'senha123',
    'usuario': 'senha456'
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username] == password:
        return f"Bem-vindo, {username}!"
    else:
        return "Usuário ou senha inválidos."

if __name__ == '__main__':
    app.run(debug=True)
