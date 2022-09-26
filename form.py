# app.py

import os
from flask import Flask
from flask import request, render_template
from flaskext.mysql import MySQL


mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'produto'
app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['DB_SERVICE'] = '172.17.0.16'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('formulario.html')

@app.route('/gravar', methods=['POST','GET'])
def gravar():
  nome = request.form['nome']
  preco = request.form['preco']
  categoria = request.form['categoria']
  if nome and preco and categoria:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into produtos (nome,preco,categoria) VALUES (%s, %s, %s)', (nome, preco, categoria))
    conn.commit()
  return render_template('formulario.html')

@app.route('/', methods=['GET', 'POST'])
def listar():
  conn = mysql.connect()
  cursor = conn.cursor() #abre uma seção dentro da conexão
  cursor.execute('select nome, preco, categoria FROM produtos')
  data = cursor.fetchall() #recuperar registros
  conn.commit()
  return render_template('lista.html', datas=data)





if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port)
