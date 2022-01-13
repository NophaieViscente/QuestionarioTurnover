import sqlite3
from sqlite3.dbapi2 import Cursor
from flask import Flask, render_template,request
from flask_restful import Resource, Api
import json

def conexaoBanco():
    conexao = sqlite3.connect('desligamento.db')
    conexao.row_factory = sqlite3.Row
    return conexao

app = Flask(__name__)

@app.route('/')
def index() :
        return render_template('index.html')

@app.route('/report')
def report() :
        conn = conexaoBanco()
        detalhes_  = conn.execute('SELECT * FROM desligamento').fetchall()
        conn.close()
        return render_template('report.html', desligamento=detalhes_)


@app.route('/add', methods=['GET','POST'])
def add_Dados() :
    if request.method == 'GET' :
        return render_template('add_turnover.html')
    else :
        values = (request.form['matricula'],
        request.form['satis_trabRadios'],
        request.form['satis_supRadios'],
        request.form['satis_colRadios'],
        request.form['satis_refRadios'],
        request.form['satis_instRadios'],
        request.form['satis_salRadios'],
        request.form['satis_benRadios'],
        request.form['atr_supRadios'],
        request.form['atr_colRadios'],
        request.form['transRadios'])
        insert_turnover(values)
        return render_template('add_success.html')

def insert_turnover(valores_insercao) :
    conn = conexaoBanco()
    c = conn.cursor()
    sql_query = """INSERT INTO desligamento (matricula, satis_trab, satis_sup, satis_colegas, satis_refeitorio, 
                                        satis_instalacoes, satis_salario, satis_benef, atritos_sup, atritos_colegas,
                                        utiliza_transp) VALUES (?,?,?,?,?,?,?,?,?,?,?)"""
    c.execute(sql_query,valores_insercao)
    conn.commit()
    conn.close()

if __name__ == '__main__' :
    app.run()