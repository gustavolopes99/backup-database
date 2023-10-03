'''
from time import strftime, time
import subprocess
import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import schedule
from bkp_connectionstring import connectionstring


class BackupGUI:
    def __init__(self):
        self.root = Tk()
        self.MainWin()
        self.root.title("Backup PostgreSQL")
        self.root.geometry("271x130")
        # self.root.resizable("false", "false")
        self.getcon = connectionstring()  # cria objeto da classe connectionstring
        self.getcon.createdatabase()
        self.root.mainloop()

    def MainWin(self):
        self.hour = ttk.Spinbox(
            self.root, from_=0, to=23, wrap=True, width=2, state="readonly"
        )
        self.hour.place(relx=0.3, rely=0.5, anchor=E)
        self.lbl_manual = Button(
            self.root, text="Backup Manual", command=self.manualbkp, width=13
        )
        self.lbl_manual.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.lbl_auto = Button(
            self.root, text="Configurar", command=self.scheduler_win, width=13
        )
        self.lbl_auto.place(relx=0.5, rely=0.5, anchor=CENTER)
        findfb = Button(
            self.root, text="Diretório Firebird", command=self.GetFBDir, width=13
        )
        # findfb.grid(row=2, column=5, pady=5, padx=5)
        btn = Button(self.root, command=self.getDataFields, text="getdata", width=13)
        btn.place(relx=0.5, rely=0.7, anchor=CENTER)

    def GetFBDir(self):
        fb_dir = filedialog.askdirectory(initialdir="C:", title="Firebird BIN")
        if len(fb_dir) > 3:
            print(fb_dir)
            self.GetfirebirdDir(fb_dir)

    def DestinationFolder(self):
        destination = filedialog.askdirectory(initialdir="C:", title="Pasta destino")
        if len(destination) > 3:
            print(destination)
            self.entry_destino.insert(0, destination)

    def GetPGDir(self):
        self.pg_dir = filedialog.askdirectory(initialdir="C:", title="Postgres BIN")
        if len(self.pg_dir) > 3:
            print(self.pg_dir)

    def GetfirebirdDir(self, fb):
        self.getcon.cursor.execute(
            f"""UPDATE TCONFIG SET DIRETORIOFIREBIRD = '{fb}' WHERE ID = 1"""
        )
        self.getcon.connection.commit()

    def GetPostgresDir(self, pg):
        self.getcon.cursor.execute(
            f"""UPDATE TCONFIG SET DIRETORIOPOSTGRES = '{pg}' WHERE ID = 1"""
        )
        self.getcon.connection.commit()

    def getDataFields(self):
        self.getcon.Firebird_dir()
        self.getcon.Postgres_dir()

    def scheduler_win(self):
        self.auto_bkp = Toplevel(self.root)
        self.auto_bkp.config(padx=5, pady=8)
        self.auto_bkp.title("Configurar")
        self.segunda = BooleanVar()
        self.terca = BooleanVar()
        self.quarta = BooleanVar()
        self.quinta = BooleanVar()
        self.sexta = BooleanVar()
        self.sabado = BooleanVar()
        self.domingo = BooleanVar()
        self.sunday = Checkbutton(
            self.auto_bkp,
            text="D",
            variable=self.domingo,
            onvalue=True,
            offvalue=False,
        )
        self.sunday.grid(column=5, row=1)
        self.monday = Checkbutton(
            self.auto_bkp,
            text="S",
            variable=self.segunda,
            onvalue=True,
            offvalue=False,
        )
        self.monday.grid(column=6, row=1)
        self.tuesday = Checkbutton(
            self.auto_bkp,
            text="T",
            variable=self.terca,
            onvalue=True,
            offvalue=False,
        )
        self.tuesday.grid(column=7, row=1)
        self.wednesday = Checkbutton(
            self.auto_bkp,
            text="Q",
            variable=self.quarta,
            onvalue=True,
            offvalue=False,
        )
        self.wednesday.grid(column=8, row=1)
        self.thursday = Checkbutton(
            self.auto_bkp,
            text="Q",
            variable=self.quinta,
            onvalue=True,
            offvalue=False,
        )
        self.thursday.grid(column=9, row=1)
        self.friday = Checkbutton(
            self.auto_bkp,
            text="S",
            variable=self.sexta,
            onvalue=True,
            offvalue=False,
        )
        self.friday.grid(column=10, row=1)
        self.saturday = Checkbutton(
            self.auto_bkp,
            text="S",
            variable=self.sabado,
            onvalue=True,
            offvalue=False,
        )
        self.saturday.grid(column=11, row=1)
        self.label_time = Label(self.auto_bkp, text="Hora HH:MM")
        self.label_time.grid(column=12, row=0)
        self.sch_time = Entry(self.auto_bkp, width=6)
        self.sch_time.grid(column=12, row=1, padx=8, pady=2)
        label_db = Label(self.auto_bkp, text="Banco de dados")
        label_db.grid(row=0, column=0, sticky=W, padx=5)
        self.db = Entry(self.auto_bkp, width=18)
        self.db.insert(0, "ecodados")
        self.db.grid(row=1, column=0, padx=5)
        user_label = Label(self.auto_bkp, text="Usuário")
        user_label.grid(row=0, column=1, sticky=W)
        self.user = Entry(self.auto_bkp, width=12)
        self.user.insert(0, "postgres")
        self.user.grid(row=1, column=1, padx=2)
        password_label = Label(self.auto_bkp, text="Senha")
        password_label.grid(row=0, column=2, sticky=W)
        self.password = Entry(self.auto_bkp, show="*", width=12)
        self.password.insert(0, "postgres")
        self.password.grid(row=1, column=2, padx=5)
        label_protocol = Label(self.auto_bkp, text="IP")
        label_protocol.grid(row=0, column=3, padx=5, sticky=W)
        self.protocol = Entry(self.auto_bkp, width=12)
        self.protocol.insert(0, "127.0.0.1")
        self.protocol.grid(row=1, column=3, padx=5, sticky=W)
        label_port = Label(self.auto_bkp, text="Porta")
        label_port.grid(row=0, column=4, sticky=W)
        self.port_entry = Entry(self.auto_bkp, width=8)
        self.port_entry.insert(0, "5432")
        self.port_entry.grid(row=1, column=4, padx=5, sticky=W)
        lbl_identify = Label(self.auto_bkp, text="Identificação")
        lbl_identify.grid(row=2, column=0, padx=5, sticky=W)
        self.identify = Entry(self.auto_bkp, width=18)
        self.identify.grid(row=3, column=0, padx=5)
        self.save = Button(
            self.auto_bkp, command=self.checkinfo, text="Salvar", width=15, height=5
        )
        self.save.grid(row=4, column=12, sticky=SE)
        lbl_findpg = Label(self.auto_bkp, text="BIN PostgreSQL")
        lbl_findpg.grid(row=2, column=1, sticky=W)
        findpg = Button(self.auto_bkp, text="Procurar", command=self.GetPGDir, width=13)
        findpg.grid(row=3, column=1, pady=5, padx=5)
        lbl_destino = Label(self.auto_bkp, text="Destino do Backup")
        lbl_destino.grid(row=2, column=3, sticky=W, columnspan=2)
        self.entry_destino = Entry(self.auto_bkp, width=29)
        self.entry_destino.grid(row=3, column=3, columnspan=2)
        self.btn_destino = Button(
            self.auto_bkp, command=self.DestinationFolder, text="...", width=6
        )
        self.btn_destino.grid(row=3, column=6)
        columns = ("ID", "Banco", "Destino")
        tree = ttk.Treeview(self.auto_bkp, columns=columns, show="headings")
        tree.heading("ID", text="Identificação")
        tree.heading("Banco", text="Nome do Banco")
        tree.heading("Destino", text="Destino")
        tree.grid(row=4, column=0, columnspan=8)

    def checkinfo(self):
        if self.sch_time.get():
            if self.protocol.get():
                if self.port_entry.get():
                    if self.db.get():
                        if self.user.get():
                            if self.password.get():
                                if self.identify.get():
                                    if self.entry_destino.get():
                                        self.saveconfig(
                                            self.pg_dir,
                                            self.port_entry.get(),
                                            self.db.get(),
                                        )

    def saveconfig(self, pgdir, pgport, banco):
        self.getcon.cursor.execute(
            f"""UPDATE TCONFIG
                                    SET DIRETORIOPOSTGRES='{pgdir}', PORTACONEXAOPG={pgport}"""
        )
        self.getcon.cursor.execute(f"""UPDATE TBASES
                                    SET BANCO='{banco}',
                                        DOMINGO='{}',
                                        SEGUNDA='{}',
                                        TERCA='{}',
                                        QUARTA='{}',
                                        QUINTA='{}',
                                        SEXTA='{}',
                                        SABADO='{}',
                                        HORA='{}',
                                        DESCRICAO='{}',
                                        MANTERBACKUP='N',
                                        BANCODEDADOS='{}',
                                        TIPOBASE='PG',
                                        USUARIOPG='{}',
                                        SENHAPG='{}',
                                        USUARIOFB='sysdba'
                                        SENHAFB='masterkey'
                                        where ID = 1  """
                                     )

    def switchstate(self):
        self.getweek = (
            self.domingo.get(),
            self.segunda.get(),
            self.terca.get(),
            self.quarta.get(),
            self.quinta.get(),
            self.sexta.get(),
            self.sabado.get(),
        )
        self.hora = self.sch_time.get()

    def scheduler(self):
        self.switchstate()
        print("Array criado:")
        for dia in self.getweek:
            print(f"{dia}", sep="\n")
        dia_arr = []
        if self.getweek[0] == True:
            dia_arr += ["domingo"]
        if self.getweek[1] == True:
            dia_arr += ["segunda"]
        if self.getweek[2] == True:
            dia_arr += ["terca"]
        if self.getweek[3] == True:
            dia_arr += ["quarta"]
        if self.getweek[4] == True:
            dia_arr += ["quinta"]
        if self.getweek[5] == True:
            dia_arr += ["sexta"]
        if self.getweek[6] == True:
            dia_arr += ["sabado"]
        print("Arrays true:")
        for sem in dia_arr:
            print(sem, sep="\n")  # Exibem os dias da semana marcados

    def manualbkp(self):
        self.manual_bkp = Toplevel(self.root)
        label_db = Label(self.manual_bkp, text="Banco de dados")
        label_db.pack()
        self.db = Entry(self.manual_bkp, justify=CENTER)
        self.db.insert(0, "ecodados")
        self.db.pack()
        user_label = Label(self.manual_bkp, text="User")
        user_label.pack()
        self.user = Entry(self.manual_bkp, justify=CENTER)
        self.user.insert(0, "postgres")
        self.user.pack()
        password_label = Label(self.manual_bkp, text="Password")
        password_label.pack()
        self.password = Entry(self.manual_bkp, show="*", justify=CENTER)
        self.password.insert(0, "postgres")
        self.password.pack()
        self.appoint = Button(
            self.manual_bkp, command=self.scheduler_win, text="Agendar"
        )
        self.appoint.pack()
        self.backup = Button(self.manual_bkp, command=self.backup_pg, text="Backup")
        self.backup.pack()

    def getinfo(self):
        self.pg_port = self.port_entry.get()

    def getip(self):
        self.pg_ip = self.protocol.get()

    def getdb(self):
        self.pg_db = self.db.get()

    def userpg(self):
        self.user_pg = self.user.get()

    def passpg(self):
        self.pass_pg = self.password.get()

    def dump(self):
        self.dumper = f""" "{self.getcon.pgdir}/pg_dump" -U %s -Z 9 -f %s -F c %s  """
        print(self.dumper)

    def backup_pg(self):
        self.getip()
        self.getport()
        self.version_pg()
        self.getdb()
        self.userpg()
        self.passpg()
        os.putenv("PGPASSWORD", self.pass_pg)
        time = str(strftime("%Y-%m-%d-%H-%M"))
        file_name = self.pg_db + "_" + time + ".sql.pgdump"
        command = self.dumper % (
            self.user_pg,
            "C:\\TemporaryBackup\\" + file_name,
            self.pg_db,
        )
        subprocess.call(command, shell=True)


if __name__ == "__main__":
    BackupGUI()

# dump using PostgreSQL's custom format, with maximum compression. (-F c, -Z 9)

"""
# dumper = (
#  "c:\\program files\\postgresql\\15\\bin\\pg_dump" -U %s -Z 9 -f %s -F c %s
# )
# os.putenv("PGPASSWORD", PASS)
# time = str(strftime("%Y-%m-%d-%H-%M"))
# file_name = database + "_" + time + ".sql.pgdump"
# Run the pg_dump command to the right directory
# command = dumper % (USER, BACKUP_DIR + file_name, database)
# subprocess.call(command, shell=True) """
'''