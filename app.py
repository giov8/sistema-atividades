from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/') #rota para a página inicial
def home():
    return render_template('index.html')

@app.route('/login') #rota para a página de login
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)