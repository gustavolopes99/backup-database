from tkinter import Tk, Frame, PhotoImage, Button, messagebox, Label


class Windows:
    verde_claro = "#606c38"
    verde_escuro = "#283618"
    bege = "#fefae0"
    marrom_claro = "#dda15e"
    marrom_escuro = "#bc6c25"
    navy = "#0a1172"
    white = "#ffffff"

    def __init__(self):
        self.root = Tk()
        self.config()
        self.frames()
        self.widgets()
        self.root.mainloop()

    def config(self):
        self.root.title("EcoBackup")
        self.root.geometry("800x600+300+80")
        self.root.iconbitmap("images/bkp.ico")
        self.root.configure(bg=self.navy)

    def frames(self):
        self.frame_superior = Frame(self.root, bg=self.white)
        self.frame_superior.place(relwidth=0.80, relheight=0.43, relx=0.10, rely=0.15)

        self.frame_inferior = Frame(self.root, bg=self.white)
        self.frame_inferior.place(relwidth=0.80, relheight=0.11, relx=0.10, rely=0.70)

    def widgets(self):
        self.img_btn1 = PhotoImage(file="images/bkp.png")
        self.btn1 = Button(
            self.frame_inferior,
            image=self.img_btn1,
            border=0,
            activebackground=self.navy,
            bg=self.white,
            command=self.show,
        )
        self.btn1.place(relx=0.15, rely=0)

    def show(self):
        self.img_bkp = PhotoImage(file="images/hd.png")
        self.label_bkp = Label(self.frame_superior, image=self.img_bkp, bg=self.white)
        self.label_bkp.place(relx=0.30, rely=0)

    def button(self):
        messagebox.showinfo("Mensagem", "Working!")


w1 = Windows()
