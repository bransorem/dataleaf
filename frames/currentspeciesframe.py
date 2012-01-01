# ====================================================
# Author: Brannen Sorem ==============================
# Date Created: 05-09-11 =============================
# ====================================================
# Modified: 05-09-11 =================================
# ====================================================

from tkinter import *

# ====================================================
# ============ Species Frame =========================
# ====================================================

class CurrentSpeciesFrame():
    ''' Describes the layout of the top/left current species area '''
    
    def __init__(self, master, interface):
        ''' Initialize current species frame '''
        
        self.interface = interface
        
        spec_frame = LabelFrame(master, text='Current Species', padx=10, pady=10)
        self.make_frame(spec_frame)
        spec_frame.pack(side=LEFT)
        
                
        
    def make_frame(self, master):
        ''' Build current species frame widgets '''
        
        self.spec_label = Label(master)
        self.spec_label['text'] = 'Species Name: '
        
        self.interface.current_species_var = StringVar()
        self.spec_name = Label(master)
        self.spec_name['textvariable'] = self.interface.current_species_var
        self.interface.current_species_var.set('None')
        
        self.view()
        
        
    def view(self):
        ''' Add widgets to frame '''
        
        self.spec_label.grid(row=0, column=0)
        self.spec_name.grid(row=0, column=1)
        

