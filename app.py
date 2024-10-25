from flask import Flask, render_template, request
app = Flask(__name__)

# Cria uma lista e usuários e senha, depois vamos pegar no DB
usuarios = {
    'admin' : 'admin',
    'usuario' : 'senha',
    'rafaela' : '111111',
    'heitor' : '1271'
}

@app.route('/') #rota para a página inicial
def home():
    return render_template('index.html')

@app.route('/login') #rota para a página de login
def login():
    return render_template('login.html')

# parte principal do
if __name__ == '__main__':
    app.run(debug=True)