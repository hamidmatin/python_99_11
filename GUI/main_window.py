from tkinter import *


class MainWindow:
    def __init__(self):
        self.__initialize()

    def __initialize(self):
        self.__mw = Tk()
        self.__mw.title("My Python Project")
        self.__mw.geometry('900x300')

        ########
        self.__lbl1 = Label(self.__mw,
                            text="Hello Python",
                            font=("Arial Bold", 50),
                            padx=50,
                            pady=30,
                            fg='red',
                            bg='pink')
        self.__lbl1.grid(column=0, row=0)

        ###############
        self.__btn1 = Button(self.__mw,
                             text="Ckick Me",
                             command=self.__btn1_click_handler)
        self.__btn1.grid(column=0, row=1)

        ###########
        self.__txt1 = Entry(self.__mw, width=40)
        self.__txt1.grid(column=0, row=2, pady=30)

        self.__btn2 = Button(self.__mw,
                             text="Click Me",
                             command=self.__btn2_click_handler)
        self.__btn2.grid(column=1, row=2)

        self.__gender = IntVar()
        
        lframe1 = LabelFrame(self.__mw, text="Gender")
        lframe1.grid(column=0, row=3)
        self.__male = Radiobutton(lframe1,text='Male', value=1, variable=self.__gender)
        self.__male.grid(column=0, row=1)
        self.__female = Radiobutton(lframe1,text='Female', value=2, variable=self.__gender)
        self.__female.grid(column=1, row=1)
        
        self.__select = IntVar()
        lframe2 = LabelFrame(self.__mw, text="Gender")
        lframe2.grid(column=1, row=3)
        self.__rd1 = Radiobutton(lframe2,text='Select 1', value=1, variable=self.__select)
        self.__rd1.grid(column=0, row=1)
        self.__rd2 = Radiobutton(lframe2,text='Select 2', value=2, variable=self.__select)
        self.__rd2.grid(column=1, row=1)
        self.__rd3 = Radiobutton(lframe2,text='Select 3', value=3, variable=self.__select)
        self.__rd3.grid(column=3, row=1)
        

        
        self.__txt1.focus()

    def show(self):
        self.__mw.mainloop()

    def __btn1_click_handler(self):
        self.__lbl1.configure(text="Button was clicked !!",
                              fg='black',
                              font=('Arial', 16))

    def __btn2_click_handler(self):
        self.__lbl1.configure(text=f"Hello {self.__txt1.get()}")
