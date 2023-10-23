import os
from flask import Flask, jsonify, request, Response, render_template, url_for, flash, redirect
from connection import getConnection
from flask_cors import CORS
import mysql.connector

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = os.urandom(16)

app.config.from_object(__name__)


CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/ping', methods={'GET'})
def ping_pong():
    return jsonify('pong')

@app.route('/registro', methods=['GET','POST'])
def registro():
    title = 'Nuevo Registro'
    if request.method == 'GET':
        return render_template('registrar.html')
    if request.method == 'POST':
        fecha = request.form['fecha']
        numfolio = request.form['numfolio']
        remitente = request.form['remitente']
        adscripcion = request.form['adscripcion']
        asunto = request.form['asunto']
        hora = request.form['hora']
        numhojas = request.form['numhojas']
        anexos = request.form['anexos']
        derivado = request.form['derivado']
        try:
            observaciones = request.form['observaciones']
            cnx = getConnection()
            cur = cnx.cursor()
            cur.execute("INSERT INTO ()VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", ())
            if cur.with_rows == True:
                flash('Registro Realizado')
                return redirect(url_for('list'))
        except mysql.connector.Error as e:
            return e
    return redirect(url_for('list'))
        #flash('Registro Realizado')
    #return 'registro reaLIZADO'    


@app.route('/list', methods={'GET'})
def list():
    title = 'Listado General'
    if request.method == 'GET':
        try:
            cnx = getConnection()
            cur = cnx.cursor()
            cur.execute("SELECT * FROM ")
            results = cur.fetchall()
            #print(results)
            cur.close()
            cnx.close()
        except mysql.connector.Error as e:
            print(e)
    return render_template('list.html', title=title, results=results)
    """return jsonify({
        'status': 'success',
        'results': results
    })"""


@app.route('/folio/<int:id>', methods=['GET'])
def getFolio(id):
    title = "Hola"
    id = id
    if request.method == 'GET':
        try:
            cnx = getConnection()
            cur = cnx.cursor()
            cur.execute("SELECT * FROM WHERE id={}".format(id))
            result = cur.fetchone()
            cur.close()
            cnx.close()
        except mysql.connector.Error as e:
            return e
    
    return jsonify({
        'status': 'OK',
        'row': result
        })

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    id=id
    if request.method == 'POST':
        cnx =getConnection()
        cur = cnx.cursor()
        cur.execute("DELETE FROM  WHERE id=?",(id))
        if cur.with_rows == True:
            print('registro ELiminado')         
        cur.close()
        cnx.close()
    return jsonify({
        'msg': 'Registro Eliminado'
    })

if __name__ == '__main__':
    app.run(debug=True)
