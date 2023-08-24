from tkinter import *
import time


class PopUp(Tk):
    def __init__(self):
        Tk.__init__(self)

        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        popup = Toplevel(self, background="gray15")
        popup.wm_title("EMAIL")
        self.withdraw()
        popup.tkraise(self)

        topframe = Frame(popup)
        topframe.grid(column=0, row=0)

        bottomframe = Frame(popup)
        bottomframe.grid(column=0, row=1)

        self.c1 = Checkbutton(
            topframe,
            text="Current",
            variable=CheckVar1,
            onvalue=1,
            offvalue=0,
            height=2,
            width=15,
        )
        self.c1.pack(side="left", fill="x")
        self.c2 = Checkbutton(
            topframe,
            text="-1",
            variable=CheckVar2,
            onvalue=1,
            offvalue=0,
            height=2,
            width=15,
        )

        self.c2.pack(side="left", fill="x")
        label = Label(
            bottomframe,
            text="Please Enter Email Address",
            background="gray15",
            foreground="snow",
        )
        label.pack(side="left", fill="x", pady=10, padx=10)
        self.entry = Entry(
            bottomframe, bd=5, width=35, background="gray30", foreground="snow"
        )
        self.entry.pack(side="left", fill="x")
        self.button = Button(
            bottomframe,
            text="OK",
            command=self.on_button,
            background="gray15",
            foreground="snow",
        )
        self.button.pack(side="left", padx=10)

    def on_button(self):
        address = self.entry.get()
        print(address)
        time.sleep(10)
        self.destroy()


app = PopUp()
app.mainloop()
