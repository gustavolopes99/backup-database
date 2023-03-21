import tkinter as tk
from tkinter import ttk
import findeco
import destino_bkp


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

        # Button
        self.basedados = findeco.Findeco()
        self.button = ttk.Button(self.widgets_frame, text="Base de dados", style="Toggle.TButton", command=lambda: self.basedados.open_eco())
        self.button.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")

        # Accentbutton
        self.target = destino_bkp.Destinobkp()
        self.accentbutton = ttk.Button(self.widgets_frame, text="Destino", style="Toggle.TButton", command=lambda: self.target.destino_bkp())
        self.accentbutton.grid(row=7, column=0, padx=5, pady=10, sticky="nsew")

        # Togglebutton
        self.backupeco = findeco.Backupeco()
        self.togglebutton = ttk.Button(self.widgets_frame, text="Backup", style="Accent.TButton", command=lambda: self.backupeco.backup_eco())
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
        self.treeview = ttk.Treeview(
            self.pane_1,
            selectmode="browse",
            yscrollcommand=self.scrollbar.set,
            columns=(1, 2),
            height=10,
        )
        self.treeview.pack(expand=True, fill="both")
        self.scrollbar.config(command=self.treeview.yview)

        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Backup Dados")
    root.resizable('false', 'false')

    # Simply set the theme
    root.tk.call("source", "azure.tcl")
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
