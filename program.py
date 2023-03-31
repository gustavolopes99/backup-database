import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from zipfile import ZipFile
import fdb
import os
import shutil
from datetime import datetime


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create a Frame for input widgets
        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
        self.widgets_frame.columnconfigure(index=0, weight=1)

        def open_eco():
            global dirfilename, filename, result, ecofile           
            dirfilename = filedialog.askopenfilename(
            initialdir='C:/ecosis/dados', 
            title='Selecione um arquivo', 
            filetypes=(('Base de dados', '*.eco'), ('All files','*.*')))           
            if len(dirfilename) > 0:
                filename = os.path.basename(dirfilename) #Get the filename without directory
                remsubstr = filename[:-3]
                result = remsubstr + 'GBK'
                print(f'Database: {filename}')
                print(f'Gbak target: {result}')
                ecofile = True
                validate_dir()

        def backup_eco():
            now = datetime.now()
            date_time = now.strftime("%d%m%y%H%M")
            path = "C:/TemporaryBackup/"
            isExist = os.path.exists(path)
            if not isExist:
                os.makedirs(path)
                print("Creating directory..")
            filecopy = shutil.copy(dirfilename, path)
            getEco = path + filename #Temporary folder directory with file added .eco
            getGbk = path + result #Temporary folder directory with file added .gbk
            svc = fdb.services.connect(password='masterkey')
            print ("Fetch materialized")
            print ("==================")
            print ("Start backup")
            svc.backup(getEco, getGbk)
            print ("svc.fetching is"), svc.fetching
            print ("svc.running is"), svc.isrunning()
            report = svc.readlines()
            print ("All lines of backup:")
            for i in report:
                print(i)
            print('Backup done...')
            svc.close()
            print('Removing database..'), os.remove(getEco)
            os.rename(getGbk, path + date_time + '_' + result)
            print(path + date_time + result)
            getPath = path + date_time + '_' + result
            print(f'Renamed to filedate')        
            print('Calling zip..')
            removeGbk = getPath[:-3] #Removing .gbk on string
            getzipFile = removeGbk + 'zip' #Adding .zip extension
            zip = ZipFile(getzipFile, "w")
            zip.write(getPath)
            print('Compressed file: ')
            print(getzipFile)
            print('Closing zip..')
            zip.close()
            print('Moving the .zip file on destination folder')
            shutil.move(getzipFile, destinopath)
            print('Removing .Gbk file')
            os.remove(getPath)
            print('Done!')

        def validate_dir():
            if ecofile == True and destino == True:
                self.togglebutton['state'] = tk.NORMAL


        def destino_bkp():
            global destinopath, destino
            destinopath = filedialog.askdirectory(initialdir='C:', title='Destino Backup')
            print(destinopath)
            destino = True
            validate_dir()
                

        def appointment():
            auto_bkp = tk.Tk()
            auto_bkp.title("Agendamento de backup")
            auto_bkp.tk.call("source", "azure.tcl")
            auto_bkp.tk.call("set_theme", "light")

            auto_bkp.update()
            auto_bkp.minsize(auto_bkp.winfo_width(), root.winfo_height())
            x_cordinate = int((auto_bkp.winfo_screenwidth() / 2) - (auto_bkp.winfo_width() / 2))
            y_cordinate = int((auto_bkp.winfo_screenheight() / 2) - (auto_bkp.winfo_height() / 2))
            auto_bkp.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

            segunda = tk.BooleanVar()
            terca = tk.BooleanVar()
            quarta = tk.BooleanVar()
            quinta = tk.BooleanVar()
            sexta = tk.BooleanVar()
            sabado = tk.BooleanVar()
            domingo = tk.BooleanVar()

            check_1 = ttk.Checkbutton(auto_bkp, text="Segunda-feira", variable=segunda)
            check_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

            check_2 = ttk.Checkbutton(auto_bkp, text="Terça-Feira", variable=terca)
            check_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

            check_3 = ttk.Checkbutton(auto_bkp, text="Quarta-Feira", variable=quarta)
            check_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

            check_4 = ttk.Checkbutton(auto_bkp, text="Quinta-feira", variable=quinta)
            check_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

            check_4 = ttk.Checkbutton(auto_bkp, text="Sexta-feira", variable=sexta)
            check_4.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")

            check_4 = ttk.Checkbutton(auto_bkp, text="Sábado", variable=sabado)
            check_4.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")

            check_4 = ttk.Checkbutton(auto_bkp, text="Domingo", variable=domingo)
            check_4.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")

        # Button
        self.button = ttk.Button(self.widgets_frame, text="Agendar", style="Toggle.TButton", command=appointment)
        self.button.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")

        self.button = ttk.Button(self.widgets_frame, text="Base de dados", style="Toggle.TButton", command=open_eco)
        self.button.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")

        # Accentbutton
        self.accentbutton = ttk.Button(self.widgets_frame, text="Destino", style="Toggle.TButton", command=destino_bkp)
        self.accentbutton.grid(row=7, column=0, padx=5, pady=10, sticky="nsew")

        # Togglebutton
        self.togglebutton = ttk.Button(self.widgets_frame, text="Backup", style="Accent.TButton", command=backup_eco, state='disable')
        self.togglebutton.grid(row=8, column=0, padx=5, pady=10, sticky="nsew")            
        

        # Panedwindow
        self.paned = ttk.PanedWindow(self)
        self.paned.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)

        # Pane #1
        self.pane_1 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_1, weight=1)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.pane_1)
        self.scrollbar.pack(side="right", fill="y")

        # Treeview
        self.treeview = ttk.Treeview(self.pane_1, selectmode="browse", yscrollcommand=self.scrollbar.set, columns=(1, 2), height=10)
        self.treeview.pack(expand=True, fill="both")
        self.scrollbar.config(command=self.treeview.yview)

        self.pane_2 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_2, weight=3)

        # Notebook, pane #2
        self.notebook = ttk.Notebook(self.pane_2)
        self.notebook.pack(fill="both", expand=True)

        # Tab #1
        self.tab_1 = ttk.Frame(self.notebook)
        for index in [0, 1]:
            self.tab_1.columnconfigure(index=index, weight=1)
            self.tab_1.rowconfigure(index=index, weight=1)
        self.notebook.add(self.tab_1, text="Informações")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Backup Dados")
    root.iconbitmap(r'c:/MVC/paper.ico')
    root.resizable('false', 'false')

    # Simply set the theme
    root.tk.call("source", r'c:/MVC/azure.tcl')
    root.tk.call("set_theme", "light")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    root.mainloop()
