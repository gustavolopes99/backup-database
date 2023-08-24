import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from zipfile import ZipFile
from tkinter import *
import fdb
import os
import shutil
from datetime import datetime
from tkinter.scrolledtext import ScrolledText


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Make the app responsive
        for indexrow in [0, 1, 2, 3]:
            self.rowconfigure(index=indexrow, weight=1)
        for indexcolumn in [0, 1, 2]:
            self.columnconfigure(index=indexcolumn, weight=1)

        # Create a Frame for input widgets
        self.main_screen = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.main_screen.grid(
            row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3
        )
        self.main_screen.columnconfigure(index=0, weight=1)

        self.buttons_panel = ttk.PanedWindow(self)
        self.buttons_panel.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)

        self.main_panel = ttk.Frame(self.buttons_panel, padding=5)
        self.buttons_panel.add(self.main_panel, weight=1)

        var_database_label = tk.StringVar()
        database_label = tk.Label(self.main_panel, textvariable=var_database_label)
        database_label.pack(expand=True, fill="both", side="bottom")

        var_dir_label = tk.StringVar()
        dir_label = tk.Label(self.main_panel, textvariable=var_dir_label)
        dir_label.pack(expand=True, fill="both", side="bottom")

        def open_eco():
            global dirfilename, filename, result, ecofile
            dirfilename = filedialog.askopenfilename(
                initialdir="C:/ecosis/dados",
                title="Selecione um arquivo",
                filetypes=(("Base de dados", "*.eco"), ("All files", "*.*")),
            )
            if len(dirfilename) > 0:
                filename = os.path.basename(
                    dirfilename
                )  # Get the filename without directory
                remsubstr = filename[:-3]
                result = remsubstr + "GBK"
                print(f"Database: {filename}")
                print(f"Gbak target: {result}")
                ecofile = True
                var_database_label.set(f"Banco de dados: {filename}")

        def backup_eco():
            now = datetime.now()
            date_time = now.strftime("%d%m%y%H%M")
            path = "C:/TemporaryBackup/"
            isExist = os.path.exists(path)
            if not isExist:
                os.makedirs(path)
                print("Creating directory..")
            filecopy = shutil.copy(dirfilename, path)
            getEco = path + filename  # Temporary folder directory with file added .eco
            getGbk = path + result  # Temporary folder directory with file added .gbk
            svc = fdb.services.connect(password="masterkey")
            print("Fetch materialized")
            print("==================")
            print("Start backup")
            svc.backup(getEco, getGbk)
            print("svc.fetching is"), svc.fetching
            print("svc.running is"), svc.isrunning()
            report = svc.readlines()
            print("All lines of backup:")
            for i in report:
                print(i)
            print("Backup done...")
            svc.close()
            print("Removing database.."), os.remove(getEco)
            os.rename(getGbk, path + date_time + "_" + result)
            print(path + date_time + result)
            getPath = path + date_time + "_" + result
            print(f"Renamed to filedate")
            print("Calling zip..")
            removeGbk = getPath[:-3]  # Removing .gbk on string
            getzipFile = removeGbk + "zip"  # Adding .zip extension
            zip = ZipFile(getzipFile, "w")
            zip.write(getPath)
            print("Compressed file: ")
            print(getzipFile)
            print("Closing zip..")
            zip.close()
            print("Moving the .zip file on destination folder")
            shutil.move(getzipFile, destinopath)
            print("Removing .Gbk file")
            os.remove(getPath)
            print("Done!")

        def validate_dir():
            if ecofile == True and destination == True:
                self.btn_bkp["state"] = tk.NORMAL

        def destino_bkp():
            global destinopath, destination
            destinopath = filedialog.askdirectory(
                initialdir="C:", title="Destino Backup"
            )
            print(destinopath)
            destination = True
            if len(destinopath) > 0:
                var_dir_label.set(f"Destino: {destinopath}")
                validate_dir()

        segunda = tk.BooleanVar()
        terca = tk.BooleanVar()
        quarta = tk.BooleanVar()
        quinta = tk.BooleanVar()
        sexta = tk.BooleanVar()
        sabado = tk.BooleanVar()
        domingo = tk.BooleanVar()

        def appointment(self):
            self.auto_bkp = tk.Tk()
            self.auto_bkp.update()
            self.auto_bkp.minsize(self.auto_bkp.winfo_width(), root.winfo_height())
            x_cordinate = int(
                (self.auto_bkp.winfo_screenwidth() / 2)
                - (self.auto_bkp.winfo_width() / 2)
            )
            y_cordinate = int(
                (self.auto_bkp.winfo_screenheight() / 2)
                - (self.auto_bkp.winfo_height() / 2)
            )
            self.auto_bkp.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

            self.auto_bkp.title("Agendamento de backup")
            self.auto_bkp.tk.call("source", "azure.tcl")
            self.auto_bkp.tk.call("set_theme", "light")

            monday = ttk.Checkbutton(
                self.auto_bkp, text="Segunda-feira", variable=segunda
            )
            monday.grid(row=0, column=0, padx=5, pady=2, sticky="nsew")

            tuesday = ttk.Checkbutton(self.auto_bkp, text="Terça-Feira", variable=terca)
            tuesday.grid(row=1, column=0, padx=5, pady=2, sticky="nsew")

            wednesday = ttk.Checkbutton(
                self.auto_bkp, text="Quarta-Feira", variable=quarta
            )
            wednesday.grid(row=2, column=0, padx=5, pady=2, sticky="nsew")

            thursday = ttk.Checkbutton(
                self.auto_bkp, text="Quinta-feira", variable=quinta
            )
            thursday.grid(row=3, column=0, padx=5, pady=2, sticky="nsew")

            friday = ttk.Checkbutton(self.auto_bkp, text="Sexta-feira", variable=sexta)
            friday.grid(row=4, column=0, padx=5, pady=2, sticky="nsew")

            saturday = ttk.Checkbutton(self.auto_bkp, text="Sábado", variable=sabado)
            saturday.grid(row=5, column=0, padx=5, pady=2, sticky="nsew")

            sunday = ttk.Checkbutton(self.auto_bkp, text="Domingo", variable=domingo)
            sunday.grid(row=6, column=0, padx=5, pady=2, sticky="nsew")

        self.console_frame = ttk.Labelframe(self.main_panel, text="Console")
        self.console_frame.pack(expand=True, fill="both")

        self.console_frame = ttk.Frame(root)
        self.console_frame.pack()

        self.scrolled_log = ScrolledText(self.main_panel, height=10, width=60)
        self.scrolled_log.configure(state="normal")
        self.scrolled_log.pack()

        self.btn_agendar = ttk.Button(
            self.main_screen,
            text="Agendar",
            style="Toggle.TButton",
            command=lambda: appointment(self),
        )
        self.btn_agendar.grid(row=0, column=0, padx=5, pady=6, sticky="nsew")

        self.btn_db = ttk.Button(
            self.main_screen,
            text="Base de dados",
            style="Toggle.TButton",
            command=open_eco,
        )
        self.btn_db.grid(row=1, column=0, padx=5, pady=6, sticky="nsew")

        self.btn_destino = ttk.Button(
            self.main_screen,
            text="Destino",
            style="Toggle.TButton",
            command=destino_bkp,
        )
        self.btn_destino.grid(row=2, column=0, padx=5, pady=6, sticky="nsew")

        self.btn_bkp = ttk.Button(
            self.main_screen,
            text="Backup",
            style="Accent.TButton",
            command=backup_eco,
            state="disable",
        )
        self.btn_bkp.grid(row=3, column=0, padx=5, pady=6, sticky="nsew")


if __name__ == "__main__":
    root = tk.Tk()
    root.eval("tk::PlaceWindow . center")
    root.title("Backup Dados")
    root.iconbitmap(r"c:/MVC/paper.ico")
    root.resizable("false", "false")

    # Simply set the theme
    root.tk.call("source", r"c:/MVC/azure.tcl")
    root.tk.call("set_theme", "light")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

    root.mainloop()
