DROP TABLE IF EXISTS desligamento;

CREATE TABLE desligamento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dta DATETIME DEFAULT (datetime(CURRENT_TIMESTAMP, 'localtime')),
    matricula INTEGER NOT NULL,
    satis_trab INTEGER NOT NULL,
    satis_sup INTEGER NOT NULL,
    satis_colegas INTEGER NOT NULL,
    satis_refeitorio INTEGER NOT NULL,
    satis_instalacoes INTEGER NOT NULL,
    satis_salario INTEGER NOT NULL,
    satis_benef INTEGER NOT NULL,
    atritos_sup INTEGER NOT NULL,
    atritos_colegas INTEGER NOT NULL,
    utiliza_transp INTEGER NOT NULL


);