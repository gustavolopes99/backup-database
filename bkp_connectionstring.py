import sqlite3


# define connection and cursor
class connectionstring:
    def __init__(self):
        connection = sqlite3.connect("pgbackup.db")

        self.cursor = connection.cursor()

        # create stores table

        self.diretfb = "C:/Program Files/firebird/Firebird_2_5/bin"
        self.diretpg = "C:/Program Files/PostgreSQL/15/bin"

        tbase = """CREATE TABLE IF NOT EXISTS
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
                        PORTA INTEGER,
                        USUARIOPG TEXT,
                        SENHAPG TEXT)"""

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
        #inserttconfig = f"""INSERT INTO TCONFIG (ID, DIRETORIOFIREBIRD, DIRETORIOPOSTGRES, CPFCNPJ, PORTACONEXAOFB, PORTACONEXAOPG, GRAVARNOSOL) VALUES ('1', {self.diretfb}, {self.diretpg}, '', '')"""

        self.cursor.execute(tbase)
        self.cursor.execute(tconfig)
        self.cursor.execute(tdiretorios)
'''
    def getConfig(self):
        selectdata = """SELECT  FROM TCONFIG"""
        self.cursor.execute
        get = """INSERT INTO """

    def firebird(self):
        getdir = """INSERT INTO TCONFIG (DIRETORIOFI) """
'''