from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

#- página sobre eu
@app.route('/sobre')
def sobre():
    return render_template("sobre.html")


#página com minha experiência profissional
@app.route('/experiencia')
def experiencia():
    return render_template("experiencia.html")

#página com sua formação acadêmica
@app.route('/formacao')
def formacao():
    return render_template("formacao.html")


#página com meus contatos
@app.route('/contatos')
def contato():
    return render_template("contatos.html")


if __name__ =="__main__":
    app.run(debug=True)