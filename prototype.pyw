# ====================================================
# Author: Brannen Sorem ==============================
# Date Created: 05-09-11 =============================
# ====================================================
# Modified: 05-09-11 =================================
# ====================================================

from interface import Interface
from tkinter import *
from frames.searchframe import SearchFrame
from frames.loginframe import LoginFrame
from frames.currentspeciesframe import CurrentSpeciesFrame
from frames.navigationframe import NavigationFrame



# ============================================================
# ============== Top Frame ===================================
# ============================================================
class TopFrame():
    ''' Set top frame of interface '''

    def __init__(self, master):
        ''' Initialize Top frame - includes current species and login '''
    
        frame = Frame(master, bd=1, relief=GROOVE, padx=10, pady=10, width=780)
        frame.pack(padx=10, pady=10, ipadx=10, fill=X)

        login_frame = LoginFrame(frame, interface)
        species_frame = CurrentSpeciesFrame(frame, interface)
        
        interface.current_species = None
        
        
        
# ============================================================
# ============= Bottom Frame =================================
# ============================================================
class BottomFrame():
    ''' Set bottom frame of interface '''

    def __init__(self, master):
        ''' Initialize the Bottom frame '''
        
        frame = Frame(master, bd=1, relief=GROOVE, padx=10, pady=10, width=780)
        frame.pack(padx=10, pady=10, ipadx=10, fill=X)
        
        nav = NavigationFrame(frame, interface)
        
     

# ============================================================
# ===================== Main Window ==========================
# ============================================================


def makewindow():
    ''' Create window '''
    
    win = Tk()
    win.title('Data Leaf')
    win.geometry('770x700')
    
    top = TopFrame(win)
    bottom = BottomFrame(win)
    
    win.mainloop()



interface = Interface()
makewindow()
