from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de contatos (simulando um banco de dados)
contatos = [
    {"nome": "Larissa", "email": "larissa@gmail.com", "telefone": "8599999000", "tag": "Curso"},
    {"nome": "Alan", "email": "alan@gmail.com", "telefone": "8599774456", "tag": "Trabalho"}
]

@app.route('/')
def index():
    return render_template('index.html', contatos=contatos)

@app.route('/adicionar', methods=['POST'])
def adicionar_contato():
    # Pegando os dados do formulário
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    tag = request.form['tag']
    
    # Adicionando o novo contato à lista
    contatos.append({
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "tag": tag
    })

    # Redireciona de volta para a página principal
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
