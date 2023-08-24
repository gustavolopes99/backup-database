from time import strftime, time
import subprocess
import os
from tkinter import *
from tkinter import filedialog
import schedule
from bkp_connectionstring import connectionstring


class Postgres:
    def __init__(self):
        self.root = Tk()
        self.pg_version = [
            "PostgreSQL 9.5",
            "PostgreSQL 9.6",
            "PostgreSQL 10",
            "PostgreSQL 11",
            "PostgreSQL 12",
            "PostgreSQL 13",
            "PostgreSQL 14",
            "PostgreSQL 15",
        ]
        self.version = StringVar()  # Armazena a variavel setada no array
        self.MainWin()
        self.root.title("Backup PostgreSQL")
        self.root.geometry("300x320")
        self.root.resizable("false", "false")
        self.getcon = connectionstring()  # cria objeto da classe connectionstring
        self.root.mainloop()

    def MainWin(self):
        self.lbl_manual = Button(
            self.root, text="Backup Manual", command=self.manualbkp
        )
        self.lbl_manual.pack()
        self.lbl_auto = Button(
            self.root, text="Configurar Backup Automático", command=self.scheduler_win
        )
        self.lbl_auto.pack()
        findfb = Button(self.root, text="Diretório Firebird", command=self.GetFBDir)
        findfb.pack()
        findpg = Button(self.root, text="Diretório Postgres", command=self.GetPGDir)
        findpg.pack()

    def GetFBDir(self):
        self.fb_dir = filedialog.askdirectory(initialdir="C:", title="Firebird BIN")
        if len(self.fb_dir) > 3:
            print(self.fb_dir)

    def GetPGDir(self):
        self.pg_dir = filedialog.askdirectory(initialdir="C:", title="Postgres BIN")
        print(self.pg_dir)

    def scheduler_win(self):
        self.auto_bkp = Toplevel(self.root)
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
        self.sunday.pack(side=LEFT)
        self.monday = Checkbutton(
            self.auto_bkp,
            text="S",
            variable=self.segunda,
            onvalue=True,
            offvalue=False,
        )
        self.monday.pack(side=LEFT)
        self.tuesday = Checkbutton(
            self.auto_bkp,
            text="T",
            variable=self.terca,
            onvalue=True,
            offvalue=False,
        )
        self.tuesday.pack(side=LEFT)
        self.wednesday = Checkbutton(
            self.auto_bkp,
            text="Q",
            variable=self.quarta,
            onvalue=True,
            offvalue=False,
        )
        self.wednesday.pack(side=LEFT)
        self.thursday = Checkbutton(
            self.auto_bkp,
            text="Q",
            variable=self.quinta,
            onvalue=True,
            offvalue=False,
        )
        self.thursday.pack(side=LEFT)
        self.friday = Checkbutton(
            self.auto_bkp,
            text="S",
            variable=self.sexta,
            onvalue=True,
            offvalue=False,
        )
        self.friday.pack(side=LEFT)
        self.saturday = Checkbutton(
            self.auto_bkp,
            text="S",
            variable=self.sabado,
            onvalue=True,
            offvalue=False,
        )
        self.saturday.pack(side=LEFT)
        self.label_time = Label(self.auto_bkp, text="Hora HH:MM")
        self.label_time.pack()
        self.sch_time = Entry(self.auto_bkp)
        self.sch_time.pack(ipadx=2)
        label_protocol = Label(self.auto_bkp, text="IP")
        label_protocol.pack()
        self.protocol = Entry(self.auto_bkp, justify=CENTER)
        self.protocol.insert(0, "127.0.0.1")
        self.protocol.pack()
        label_port = Label(self.auto_bkp, text="Porta")
        label_port.pack()
        self.port_entry = Entry(self.auto_bkp, justify=CENTER)
        self.port_entry.insert(0, "5432")
        self.port_entry.pack()
        label_db = Label(self.auto_bkp, text="Banco de dados")
        label_db.pack()
        self.db = Entry(self.auto_bkp, justify=CENTER)
        self.db.insert(0, "ecodados")
        self.db.pack()
        user_label = Label(self.auto_bkp, text="User")
        user_label.pack()
        self.user = Entry(self.auto_bkp, justify=CENTER)
        self.user.insert(0, "postgres")
        self.user.pack()
        password_label = Label(self.auto_bkp, text="Password")
        password_label.pack()
        self.password = Entry(self.auto_bkp, show="*", justify=CENTER)
        self.password.insert(0, "postgres")
        self.password.pack()
        self.save = Button(self.auto_bkp, command=self.scheduler, text="Salvar")
        self.save.pack(after=self.password)

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

    def version_pg(self):
        self.get_version = self.version.get()  # armazena a variavel da StringVar
        self.v = "PostgreSQL 9.5"
        if self.get_version == self.v:
            self.dump("9.5")
        elif self.get_version == self.v.replace("9.5", "9.6"):
            self.dump("9.6")
        elif self.get_version == self.v.replace("9.5", "10"):
            self.dump("10")
        elif self.get_version == self.v.replace("9.5", "11"):
            self.dump("11")
        elif self.get_version == self.v.replace("9.5", "12"):
            self.dump("12")
        elif self.get_version == self.v.replace("9.5", "13"):
            self.dump("13")
        elif self.get_version == self.v.replace("9.5", "14"):
            self.dump("14")
        elif self.get_version == self.v.replace("9.5", "15"):
            self.dump("15")

    def manualbkp(self):
        self.manual_bkp = Toplevel(self.root)
        # versao_pg = Label(self.root, text="Versão")
        # versao_pg.pack()
        # combo_version =  (
        #    self.root, values=self.pg_version, textvariable=self.version
        # )
        # combo_version.pack()
        label_protocol = Label(self.manual_bkp, text="IP")
        label_protocol.pack()
        self.protocol = Entry(self.manual_bkp, justify=CENTER)
        self.protocol.insert(0, "127.0.0.1")
        self.protocol.pack()
        label_port = Label(self.manual_bkp, text="Porta")
        label_port.pack()
        self.port_entry = Entry(self.manual_bkp, justify=CENTER)
        self.port_entry.insert(0, "5432")
        self.port_entry.pack()
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

    def dump(self, version):
        self.dumper = f""" "c:\\program files\\postgresql\\{version}\\bin\\pg_dump" -U %s -Z 9 -f %s -F c %s  """
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


Postgres()

# dump using PostgreSQL's custom format, with maximum compression. (-F c, -Z 9)


# dumper = (
#    """ "c:\\program files\\postgresql\\15\\bin\\pg_dump" -U %s -Z 9 -f %s -F c %s  """
# )
# os.putenv("PGPASSWORD", PASS)
# time = str(strftime("%Y-%m-%d-%H-%M"))
# file_name = database + "_" + time + ".sql.pgdump"
# Run the pg_dump command to the right directory
# command = dumper % (USER, BACKUP_DIR + file_name, database)
# subprocess.call(command, shell=True)
