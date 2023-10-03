import sqlite3
from PyQt6.QtWidgets import QMessageBox


# define connection and cursor
class connectionstring:
    def __init__(self):
        try:
            self.connection = sqlite3.connect("pgbackup.db")
        except BaseException as e:
            QMessageBox.critical(self, "Erro", e)

        self.cursor = self.connection.cursor()

        # create stores table

    def reconnect(self):
        sqlite3.connect("pgbackup.db")

    def createdatabase(self):
        criartabelafb = """CREATE TABLE IF NOT EXISTS
                        TBASES (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                BANCO TEXT,
                                IP TEXT,
                                PORTA INTEGER,
                                USUARIO TEXT,
                                SENHA TEXT,
                                IDENTIFICACAO TEXT,
                                DESTINO TEXT,
                                DOMINGO TEXT,
                                SEGUNDA TEXT,
                                TERCA TEXT,
                                QUARTA TEXT,
                                QUINTA TEXT,
                                SEXTA TEXT,
                                SABADO TEXT,
                                HORA TEXT)
                          """
        self.cursor.execute(criartabelafb)


'''tbasefirebird = """CREATE TABLE IF NOT EXISTS
            TBASES (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    BANCO TEXT,
                    DOMINGO INTEGER,
                    SEGUNDA INTEGER,
                    TERCA INTEGER,
                    QUARTA INTEGER,
                    QUINTA INTEGER,
                    SEXTA INTEGER,
                    SABADO INTEGER,
                    HORA REAL,
                    DESCRICAO TEXT,
                    MANTERBACKUP INTEGER,
                    BANCODEDADOS INTEGER,
                    TIPOBASE INTEGER,
                    USUARIOPG TEXT,
                    SENHAPG TEXT,
                    USUARIOFB TEXT,
                    SENHAFB TEXT,
                    IP TEXT)"""

    tconfig = """CREATE TABLE IF NOT EXISTS TCONFIG
            (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    DIRETORIOFIREBIRD TEXT,
                    DIRETORIOPOSTGRES TEXT,
                    CPFCNPJ TEXT,
                    PORTACONEXAOFB INTEGER,
                    PORTACONEXAOPG INTEGER,
                    GRAVARNOSOL INTEGER)"""

    tdiretorios = """CREATE TABLE IF NOT EXISTS TDIRETORIOS 
                            (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            IDBASE INTEGER,
                            DIRETORIO TEXT,
                            CONSTRAINT FK_TDIRETORIOS_TBASES_IDBASE FOREIGN KEY (IDBASE) REFERENCES TBASES (ID))"""

    inserttconfig = f"""INSERT OR IGNORE INTO TCONFIG 
                            (ID, DIRETORIOFIREBIRD, DIRETORIOPOSTGRES, CPFCNPJ, GRAVARNOSOL)
                    VALUES 
                            ('1', '', '', '', 'S')"""
    insertdiretorio = f"""INSERT OR IGNORE INTO TDIRETORIOS
                            (ID, IDBASE, DIRETORIO)
                    VALUES
                            ('1', '', '')"""

    self.cursor.execute(tbase)
    self.cursor.execute(tconfig)
    self.cursor.execute(tdiretorios)
    self.selectconfig = self.cursor.execute("SELECT * FROM TCONFIG WHERE (ID = 1)")
    self.selectbases = self.cursor.execute("SELECT * FROM TBASES WHERE (ID = 1)")
    self.selectdiretorios = self.cursor.execute(
        "SELECT * FROM TDIRETORIOS WHERE (ID = 1)"
    )
    self.getconfig = self.selectconfig.fetchone()
    if self.getconfig is None:
        self.cursor.execute(inserttconfig)
        self.connection.commit()
        print("New entry added on TCONFIG")
    else:
        print("Entry found on TCONFIG")

    self.getdiretorios = self.selectdiretorios.fetchone()
    if self.getdiretorios is None:
        self.cursor.execute(insertdiretorio)
        self.connection.commit()
        print("New entry added on TDIRETORIOS")
    else:
        print("Entry found on TDIRETORIOS")

def Firebird_dir(self):
    selectfb = self.cursor.execute(
        "select diretoriofirebird from tconfig where id = 1"
    )
    fetch = selectfb.fetchone()
    self.fbdir = fetch[0]
    print(self.fbdir)

def Postgres_dir(self):
    selectfb = self.cursor.execute(
        "select diretoriopostgres from tconfig where id = 1"
    )
    fetch = selectfb.fetchone()
    self.pgdir = fetch[0]
    print(self.pgdir)

def insertData_FB(self, user, password, ip, port, hour, ident, database):
    try:
        self.cursor.execute(f"UPDATE TCONFIG SET PORTACONEXAOFB = {port}")
        self.cursor.execute(
            f"INSERT INTO TBASES (BANCO, DOMINGO, SEGUNDA, TERCA, QUARTA, QUINTA, SEXTA, SABADO, HORA, DESCRICAO, MANTERBACKUP, BANCODEDADOS, TIPOBASE, USUARIOFB, SENHAFB, IP) VALUES ('{database}','1','1','1','1','1','1','1', '{hour}', '{ident}', 'S', '1', '0', '{user}', '{password}','{ip}' )"
        )
        self.connection.commit()
    except Exception:
        print(Exception)
'''
