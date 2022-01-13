import sqlite3

conexao = sqlite3.connect('desligamento.db')


with open('schema.sql') as f:
    conexao.executescript(f.read())

cur = conexao.cursor()
conexao.commit()
conexao.close()