import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Necessária para mensagens flash

# Função para conectar ao banco de dados SQLite
def get_db_connection():
    conn = sqlite3.connect('meu_banco.db')
    conn.row_factory = sqlite3.Row 
    # Facilita acessar as colunas pelo nome
    return conn

# Inicializar o banco de dados (criar a tabela de usuários)
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Rota inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute(
            'SELECT * FROM users WHERE username = ? AND password = ?', 
            (username, password)
        ).fetchone()
        conn.close()

        if user:
            return f"Bem-vindo, {username}!"
        else:
            flash("Usuário ou senha inválidos.")
            return redirect(url_for('login'))

    return render_template('login.html')

# Rota para registrar novos usuários (para testes)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        try:
            conn.execute(
                'INSERT INTO users (username, password) VALUES (?, ?)',
                (username, password)
            )
            conn.commit()
            flash("Usuário registrado com sucesso!")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Nome de usuário já existe.")
        finally:
            conn.close()

    return render_template('register.html')

# Inicializar o banco de dados antes de iniciar o app
init_db()

if __name__ == '__main__':
    app.run(debug=True)
