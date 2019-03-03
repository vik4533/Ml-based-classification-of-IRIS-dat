# import sys
import layout
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

#import unknown_support

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
    def login(self):
        fp=open("db.csv","a+")
        use=self.TEntry1.get()
        pas=self.TEntry2.get()
        fp.write(use+","+pas+"\n")
        #self.destroy()
        layout.vp_start_gui()
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 

        top.geometry("867x623+447+114")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        # self.Label1 = tk.Label(top)
        # self.Label1.place(relx=-0.046, rely=-0.241, height=811, width=1004)
        # self.Label1.configure(background="#d9d9d9")
        # self.Label1.configure(disabledforeground="#a3a3a3")
        # self.Label1.configure(foreground="#000000")
        # self._img1 = tk.PhotoImage(file="C:/Users/VIK/Downloads/floral-png-floral-png-image-png-image-1000.png")
        # self.Label1.configure(image=self._img1)
        # self.Label1.configure(text='''Label''')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.139, rely=0.10, height=56, width=791)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="TkDefaultFont")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightcolor="#646464")
        self.Label1.configure(text='''WELCOME TO MACHINE LEARNING TRAINING AND TESTING''')
        self.Label1.configure(width=791)

  
        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.565, rely=0.209, relheight=0.361
                , relwidth=0.375)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=325)

        self.TButton1 = ttk.Button(self.Frame1,command=self.login)
        self.TButton1.place(relx=0.369, rely=0.711, height=40, width=108)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''LOGIN''')
        self.TButton1.configure(width=108)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.092, rely=0.178, height=36, width=102)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="font11")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Username''')
        self.Label1.configure(width=102)

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.123, rely=0.4, height=36, width=88)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="font11")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Password''')
        self.Label2.configure(width=88)

        self.TEntry1 = ttk.Entry(self.Frame1)
        self.TEntry1.place(relx=0.431, rely=0.178, relheight=0.16
                , relwidth=0.511)
        self.TEntry1.configure(width=166)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")

        self.TEntry2 = ttk.Entry(self.Frame1)
        self.TEntry2.place(relx=0.431, rely=0.4, relheight=0.16, relwidth=0.511)
        self.TEntry2.configure(width=166)
        self.TEntry2.configure(takefocus="")
        self.TEntry2.configure(cursor="ibeam")


if __name__ == '__main__':
    vp_start_gui()





