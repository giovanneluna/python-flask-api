from flask import Flask, make_response,jsonify,request
from bd import Carros
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='MyUser',
    password='MainPassword',
    database='concessionaire'
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/carros',methods=['GET'])
def get_carros():

    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM carros')
    meus_carros = my_cursor.fetchall()

    carros = list()
    for carro in meus_carros:
        carros.append( {
            'id': carro[0],
            'marca':carro[1],
            'modelo': carro[2],
            'ano': carro[3]
        })
    return (make_response(
      jsonify(
              message = 'Lista de carros',
              data=carros
              )
    ))

@app.route('/carros',methods=['POST'])
def create_carro():
    carro = request.json

    my_cursor = mydb.cursor()

    sql = f"INSERT INTO carros (marca,modelo,ano) VALUES ('{carro['marca']}','{carro['modelo']}',{carro['ano']})"

    my_cursor.execute(sql)
    mydb.commit()


    return (make_response(
        jsonify(
            message = 'Carro cadastrado com sucesso!',
            carro = carro
        )
    ))

@app.route('/carros/<int:id>', methods=['PUT'])
def update_carro(id):
    carro = request.json

    my_cursor = mydb.cursor()
    sql = f"UPDATE carros SET marca='{carro['marca']}', modelo='{carro['modelo']}', ano={carro['ano']} WHERE id={id}"
    my_cursor.execute(sql)
    mydb.commit()

    return make_response(
        jsonify(
            message='Carro atualizado com sucesso!',
            carro=carro
        )
    )

@app.route('/carros/<int:id>', methods=['DELETE'])
def delete_carro(id):
    my_cursor = mydb.cursor()
    sql = f"DELETE FROM carros WHERE id={id}"
    my_cursor.execute(sql)
    mydb.commit()

    return make_response(
        jsonify(
            message='Carro deletado com sucesso!'
        )
    )

app.run()