import sys
import KNN
import randomforest

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from tkinter import filedialog
from tkinter import *

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    #unknown_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    #unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:

    def selfil(self):
        filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        self.TLabel3.configure(text=filename)
    def selfil1(self):
        filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        self.TLabel4.configure(text=filename)
    ###################################################
    def trainknn(self):
        self.ww=KNN.KNN1();
        self.TLabel5.configure(text=self.ww.train(self.TLabel3.cget("text"),self.Entry113.get()))
        ##################################
    def trainrf(self):
        self.ww1=randomforest.RF()
        self.TLabel6.configure(text=self.ww1.train1(self.TLabel4.cget("text"),self.Entry112.get()))
    ###################################################
    def checkan(self):
        strw=self.ww.checkann(self.Entry1.get(),self.Entry1_8.get(),self.Entry1_9.get(),self.Entry1_10.get())
        self.Label5.configure(text="class is : "+strw)
        ########################################
    def checkrf(self):
        strw=self.ww1.checkrf(self.Entry1_16.get(),self.Entry11_9.get(),self.Entry11_10.get(),self.Entry1_11.get())
        self.Label5_13.configure(text="class is : "+strw)
    ####################################################
    def teee(self):
        filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        self.TLabel6b.configure(text=filename)
    def teee1(self):
        filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        self.TLabel6c.configure(text=filename)
    #########################################################

    def anaknn(self):
        strw=self.ww.anknn(self.TLabel6b.cget("text"))
        ########################################
    def anarf(self):
        strw=self.ww1.anrf(self.TLabel6c.cget("text"))

###################################################################
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("864x623+447+114")
        top.title("Machine Learning")
        top.configure(background="#d9d9d9")

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=-0.023, rely=0.128, relwidth=1.03)

        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=0.498, rely=0.0, relheight=0.979)
        self.TSeparator2.configure(orient="vertical")

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.139, rely=0.048, height=24, width=149)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief='flat')
        self.TLabel1.configure(text='''K Nearest Neighbours''')

        self.TLabel2 = ttk.Label(top)
        self.TLabel2.place(relx=0.625, rely=0.048, height=24, width=167)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief='flat')
        self.TLabel2.configure(text='''Random Forest Classifier''')

        self.select_file = ttk.Button(top,command=self.selfil)
        self.select_file.place(relx=0.15, rely=0.177, height=30, width=98)
        self.select_file.configure(takefocus="")
        self.select_file.configure(text='''Select File''')

        self.select_file_1 = ttk.Button(top,command=self.selfil1)
        self.select_file_1.place(relx=0.66, rely=0.177, height=30, width=98)
        self.select_file_1.configure(takefocus="")
        self.select_file_1.configure(text='''Select File''')

        self.TLabel3 = ttk.Label(top)
        self.TLabel3.place(relx=0.116, rely=0.240, height=24, width=300)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief='flat')
        self.TLabel3.configure(text='''your file:''')

        self.TLabel4 = ttk.Label(top)
        self.TLabel4.place(relx=0.637, rely=0.240, height=24, width=300)
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font="TkDefaultFont")
        self.TLabel4.configure(relief='flat')
        self.TLabel4.configure(text='''your file:''')
        self.TLabel4.configure(width=78)

        self.TButton1 = ttk.Button(top,command=self.trainknn)
        self.TButton1.place(relx=0.169, rely=0.400, height=30, width=98)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Train KNN''')

        self.TButton2 = ttk.Button(top,command=self.trainrf)
        self.TButton2.place(relx=0.66, rely=0.400, height=30, width=98)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Train RF''')

        self.Label41 = tk.Label(top)
        self.Label41.place(relx=0.065, rely=0.300, height=28, width=100)
        self.Label41.configure(background="#d9d9d9")
        self.Label41.configure(disabledforeground="#a3a3a3")
        self.Label41.configure(foreground="#000000")
        self.Label41.configure(text='''Train/Test (%/100) :''')

        self.Entry113 = tk.Entry(top)
        self.Entry113.place(relx=0.197, rely=0.300,height=24, relwidth=0.265)
        self.Entry113.configure(background="white")
        self.Entry113.configure(disabledforeground="#a3a3a3")
        self.Entry113.configure(font="TkFixedFont")
        self.Entry113.configure(foreground="#000000")
        self.Entry113.configure(insertbackground="black")
        self.Entry113.configure(width=94)

        self.Label42 = tk.Label(top)
        self.Label42.place(relx=0.550, rely=0.30, height=28, width=100)
        self.Label42.configure(background="#d9d9d9")
        self.Label42.configure(disabledforeground="#a3a3a3")
        self.Label42.configure(foreground="#000000")
        self.Label42.configure(text='''Train/Test (%/100):''')

        self.Entry112 = tk.Entry(top)
        self.Entry112.place(relx=0.700, rely=0.300,height=24, relwidth=0.265)
        self.Entry112.configure(background="white")
        self.Entry112.configure(disabledforeground="#a3a3a3")
        self.Entry112.configure(font="TkFixedFont")
        self.Entry112.configure(foreground="#000000")
        self.Entry112.configure(insertbackground="black")
        self.Entry112.configure(width=94)

        self.TLabel5 = ttk.Label(top)
        self.TLabel5.place(relx=0.127, rely=0.450, height=24, width=300)
        self.TLabel5.configure(background="#d9d9d9")
        self.TLabel5.configure(foreground="#000000")
        self.TLabel5.configure(font="TkDefaultFont")
        self.TLabel5.configure(relief='flat')
        self.TLabel5.configure(text='''Accuracy :''')

        self.TLabel6 = ttk.Label(top)
        self.TLabel6.place(relx=0.625, rely=0.450, height=24, width=300)
        self.TLabel6.configure(background="#d9d9d9")
        self.TLabel6.configure(foreground="#000000")
        self.TLabel6.configure(font="TkDefaultFont")
        self.TLabel6.configure(relief='flat')
        self.TLabel6.configure(text='''Accuracy :''')

################################################################################
        self.TButton11 = ttk.Button(top,command=self.teee)
        self.TButton11.place(relx=0.169, rely=0.500, height=30, width=98)
        self.TButton11.configure(takefocus="")
        self.TButton11.configure(text='''upload Test File''')

        self.TLabel6b = ttk.Label(top)
        self.TLabel6b.place(relx=0.169, rely=0.550, height=24, width=300)
        self.TLabel6b.configure(background="#d9d9d9")
        self.TLabel6b.configure(foreground="#000000")
        self.TLabel6b.configure(font="TkDefaultFont")
        self.TLabel6b.configure(relief='flat')
        self.TLabel6b.configure(text='''file is :''')

        self.TButton21 = ttk.Button(top,command=self.anaknn)
        self.TButton21.place(relx=0.169, rely=0.600, height=30, width=98)
        self.TButton21.configure(takefocus="")
        self.TButton21.configure(text='''Analysis''')

        ##################################################################
        
        self.TButton111 = ttk.Button(top,command=self.teee1)
        self.TButton111.place(relx=0.625, rely=0.500, height=30, width=98)
        self.TButton111.configure(takefocus="")
        self.TButton111.configure(text='''upload Test File''')

        self.TLabel6c = ttk.Label(top)
        self.TLabel6c.place(relx=0.625, rely=0.550, height=24, width=300)
        self.TLabel6c.configure(background="#d9d9d9")
        self.TLabel6c.configure(foreground="#000000")
        self.TLabel6c.configure(font="TkDefaultFont")
        self.TLabel6c.configure(relief='flat')
        self.TLabel6c.configure(text='''file is :''')

        self.TButton211 = ttk.Button(top,command=self.anarf)
        self.TButton211.place(relx=0.625, rely=0.600, height=30, width=98)
        self.TButton211.configure(takefocus="")
        self.TButton211.configure(text='''Analysis''')
###################################################################################


        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.TFrame1 = ttk.Frame(top)
        self.TFrame1.place(relx=0.046, rely=0.706, relheight=0.265
                , relwidth=0.411)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(width=355)

        self.Label1 = tk.Label(self.TFrame1)
        self.Label1.place(relx=0.056, rely=0.061, height=26, width=21)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''SL''')

        self.Label2 = tk.Label(self.TFrame1)
        self.Label2.place(relx=0.056, rely=0.364, height=26, width=21)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''PL''')

        self.Label3 = tk.Label(self.TFrame1)
        self.Label3.place(relx=0.535, rely=0.061, height=26, width=23)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''SB''')

        self.Label4 = tk.Label(self.TFrame1)
        self.Label4.place(relx=0.535, rely=0.364, height=26, width=23)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''PB''')

        self.Entry1 = tk.Entry(self.TFrame1)
        self.Entry1.place(relx=0.197, rely=0.061,height=24, relwidth=0.265)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=94)

        self.Entry1_8 = tk.Entry(self.TFrame1)
        self.Entry1_8.place(relx=0.676, rely=0.061,height=24, relwidth=0.265)
        self.Entry1_8.configure(background="white")
        self.Entry1_8.configure(disabledforeground="#a3a3a3")
        self.Entry1_8.configure(font="TkFixedFont")
        self.Entry1_8.configure(foreground="#000000")
        self.Entry1_8.configure(highlightbackground="#d9d9d9")
        self.Entry1_8.configure(highlightcolor="black")
        self.Entry1_8.configure(insertbackground="black")
        self.Entry1_8.configure(selectbackground="#c4c4c4")
        self.Entry1_8.configure(selectforeground="black")

        self.Entry1_9 = tk.Entry(self.TFrame1)
        self.Entry1_9.place(relx=0.197, rely=0.364,height=24, relwidth=0.265)
        self.Entry1_9.configure(background="white")
        self.Entry1_9.configure(disabledforeground="#a3a3a3")
        self.Entry1_9.configure(font="TkFixedFont")
        self.Entry1_9.configure(foreground="#000000")
        self.Entry1_9.configure(highlightbackground="#d9d9d9")
        self.Entry1_9.configure(highlightcolor="black")
        self.Entry1_9.configure(insertbackground="black")
        self.Entry1_9.configure(selectbackground="#c4c4c4")
        self.Entry1_9.configure(selectforeground="black")

        self.Entry1_10 = tk.Entry(self.TFrame1)
        self.Entry1_10.place(relx=0.676, rely=0.364,height=24, relwidth=0.265)
        self.Entry1_10.configure(background="white")
        self.Entry1_10.configure(disabledforeground="#a3a3a3")
        self.Entry1_10.configure(font="TkFixedFont")
        self.Entry1_10.configure(foreground="#000000")
        self.Entry1_10.configure(highlightbackground="#d9d9d9")
        self.Entry1_10.configure(highlightcolor="black")
        self.Entry1_10.configure(insertbackground="black")
        self.Entry1_10.configure(selectbackground="#c4c4c4")
        self.Entry1_10.configure(selectforeground="black")

        self.Button1 = tk.Button(self.TFrame1,command=self.checkan)
        self.Button1.place(relx=0.141, rely=0.667, height=33, width=88)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Check Class''')

        self.Label5 = tk.Label(self.TFrame1)
        self.Label5.place(relx=0.507, rely=0.667, height=26, width=200)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Output:''')

        self.TFrame1_11 = ttk.Frame(top)
        self.TFrame1_11.place(relx=0.556, rely=0.706, relheight=0.265
                , relwidth=0.411)
        self.TFrame1_11.configure(relief='groove')
        self.TFrame1_11.configure(borderwidth="2")
        self.TFrame1_11.configure(relief='groove')
        self.TFrame1_11.configure(width=355)

        self.Label1_12 = tk.Label(self.TFrame1_11)
        self.Label1_12.place(relx=0.056, rely=0.061, height=26, width=21)
        self.Label1_12.configure(activebackground="#f9f9f9")
        self.Label1_12.configure(activeforeground="black")
        self.Label1_12.configure(background="#d9d9d9")
        self.Label1_12.configure(disabledforeground="#a3a3a3")
        self.Label1_12.configure(foreground="#000000")
        self.Label1_12.configure(highlightbackground="#d9d9d9")
        self.Label1_12.configure(highlightcolor="black")
        self.Label1_12.configure(text='''SL''')

        self.Label2_13 = tk.Label(self.TFrame1_11)
        self.Label2_13.place(relx=0.056, rely=0.364, height=26, width=21)
        self.Label2_13.configure(activebackground="#f9f9f9")
        self.Label2_13.configure(activeforeground="black")
        self.Label2_13.configure(background="#d9d9d9")
        self.Label2_13.configure(disabledforeground="#a3a3a3")
        self.Label2_13.configure(foreground="#000000")
        self.Label2_13.configure(highlightbackground="#d9d9d9")
        self.Label2_13.configure(highlightcolor="black")
        self.Label2_13.configure(text='''PL''')

        self.Label3_14 = tk.Label(self.TFrame1_11)
        self.Label3_14.place(relx=0.535, rely=0.061, height=26, width=23)
        self.Label3_14.configure(activebackground="#f9f9f9")
        self.Label3_14.configure(activeforeground="black")
        self.Label3_14.configure(background="#d9d9d9")
        self.Label3_14.configure(disabledforeground="#a3a3a3")
        self.Label3_14.configure(foreground="#000000")
        self.Label3_14.configure(highlightbackground="#d9d9d9")
        self.Label3_14.configure(highlightcolor="black")
        self.Label3_14.configure(text='''SB''')

        self.Label4_15 = tk.Label(self.TFrame1_11)
        self.Label4_15.place(relx=0.535, rely=0.364, height=26, width=23)
        self.Label4_15.configure(activebackground="#f9f9f9")
        self.Label4_15.configure(activeforeground="black")
        self.Label4_15.configure(background="#d9d9d9")
        self.Label4_15.configure(disabledforeground="#a3a3a3")
        self.Label4_15.configure(foreground="#000000")
        self.Label4_15.configure(highlightbackground="#d9d9d9")
        self.Label4_15.configure(highlightcolor="black")
        self.Label4_15.configure(text='''PB''')

        self.Entry1_16 = tk.Entry(self.TFrame1_11)
        self.Entry1_16.place(relx=0.197, rely=0.061,height=24, relwidth=0.265)
        self.Entry1_16.configure(background="white")
        self.Entry1_16.configure(disabledforeground="#a3a3a3")
        self.Entry1_16.configure(font="TkFixedFont")
        self.Entry1_16.configure(foreground="#000000")
        self.Entry1_16.configure(highlightbackground="#d9d9d9")
        self.Entry1_16.configure(highlightcolor="black")
        self.Entry1_16.configure(insertbackground="black")
        self.Entry1_16.configure(selectbackground="#c4c4c4")
        self.Entry1_16.configure(selectforeground="black")

        self.Entry11_9 = tk.Entry(self.TFrame1_11)
        self.Entry11_9.place(relx=0.676, rely=0.061,height=24, relwidth=0.265)
        self.Entry11_9.configure(background="white")
        self.Entry11_9.configure(disabledforeground="#a3a3a3")
        self.Entry11_9.configure(font="TkFixedFont")
        self.Entry11_9.configure(foreground="#000000")
        self.Entry11_9.configure(highlightbackground="#d9d9d9")
        self.Entry11_9.configure(highlightcolor="black")
        self.Entry11_9.configure(insertbackground="black")
        self.Entry11_9.configure(selectbackground="#c4c4c4")
        self.Entry11_9.configure(selectforeground="black")

        self.Entry11_10 = tk.Entry(self.TFrame1_11)
        self.Entry11_10.place(relx=0.197, rely=0.364,height=24, relwidth=0.265)
        self.Entry11_10.configure(background="white")
        self.Entry11_10.configure(disabledforeground="#a3a3a3")
        self.Entry11_10.configure(font="TkFixedFont")
        self.Entry11_10.configure(foreground="#000000")
        self.Entry11_10.configure(highlightbackground="#d9d9d9")
        self.Entry11_10.configure(highlightcolor="black")
        self.Entry11_10.configure(insertbackground="black")
        self.Entry11_10.configure(selectbackground="#c4c4c4")
        self.Entry11_10.configure(selectforeground="black")

        self.Entry1_11 = tk.Entry(self.TFrame1_11)
        self.Entry1_11.place(relx=0.676, rely=0.364,height=24, relwidth=0.265)
        self.Entry1_11.configure(background="white")
        self.Entry1_11.configure(disabledforeground="#a3a3a3")
        self.Entry1_11.configure(font="TkFixedFont")
        self.Entry1_11.configure(foreground="#000000")
        self.Entry1_11.configure(highlightbackground="#d9d9d9")
        self.Entry1_11.configure(highlightcolor="black")
        self.Entry1_11.configure(insertbackground="black")
        self.Entry1_11.configure(selectbackground="#c4c4c4")
        self.Entry1_11.configure(selectforeground="black")

        self.Button1_12 = tk.Button(self.TFrame1_11,command=self.checkrf)
        self.Button1_12.place(relx=0.141, rely=0.667, height=33, width=88)
        self.Button1_12.configure(activebackground="#ececec")
        self.Button1_12.configure(activeforeground="#000000")
        self.Button1_12.configure(background="#d9d9d9")
        self.Button1_12.configure(disabledforeground="#a3a3a3")
        self.Button1_12.configure(foreground="#000000")
        self.Button1_12.configure(highlightbackground="#d9d9d9")
        self.Button1_12.configure(highlightcolor="black")
        self.Button1_12.configure(pady="0")
        self.Button1_12.configure(text='''Check Class''')

        self.Label5_13 = tk.Label(self.TFrame1_11)
        self.Label5_13.place(relx=0.507, rely=0.667, height=26, width=200)
        self.Label5_13.configure(activebackground="#f9f9f9")
        self.Label5_13.configure(activeforeground="black")
        self.Label5_13.configure(background="#d9d9d9")
        self.Label5_13.configure(disabledforeground="#a3a3a3")
        self.Label5_13.configure(foreground="#000000")
        self.Label5_13.configure(highlightbackground="#d9d9d9")
        self.Label5_13.configure(highlightcolor="black")
        self.Label5_13.configure(text='''Output:''')

if __name__ == '__main__':
    vp_start_gui()

