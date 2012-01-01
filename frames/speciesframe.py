# ====================================================
# Author: Brannen Sorem ==============================
# Date Created: 05-09-11 =============================
# ====================================================
# Modified: 05-10-11 =================================
# ====================================================

from tkinter import *

# ============================================================
# ================ Species Frame =============================
# ============================================================
class SpeciesFrame():
    ''' Species frame '''

    def __init__(self, master, interface):
        ''' Initialize species frame '''
    
        self.frame = Frame(master, padx=10, pady=10)
        self.frame.pack()
        
        self.interface = interface
        self.top = self.SpeciesTopFrame(self.frame, interface, self)
        #self.bottom = self.SpeciesBottomFrame(self.frame, interface, self)
        self.set()
        
        
    def set(self):
        ''' Set the current species details in the frame labels '''
    
        current = self.interface.current_species
        
        if current != None:
            self.top.label_scientific_name_var.set(current.genus + ' ' + current.species)
            self.top.label_common_name_var.set(current.common_name)
            self.top.label_lifeform_var.set(current.lifeform)
            self.top.label_elevation_var.set(str(current.range_low) + ' to ' + str(current.range_high) + ' m ')
        
    
    class SpeciesTopFrame():
        ''' Species top frame, all of the available information '''
    
        def __init__(self, master, interface, owner):
            ''' Initialize species top frame '''
        
            self.interface = interface
            
            self.frame = Frame(master)
            self.make_frame(self.frame)
            self.frame.pack()
            
            
        def make_frame(self, master):
            ''' Create the widgets for the top frame of species '''
        
            self.label_scientific_name_label = Label(master)
            self.label_common_name_label = Label(master)
            self.label_elevation_label = Label(master)
            self.label_lifeform_label = Label(master)
            
            self.label_scientific_name_label['text'] = 'Scientific Name:'
            self.label_common_name_label['text'] = 'Common Name:'
            self.label_elevation_label['text'] = 'Elevation Range:'
            self.label_lifeform_label['text'] = 'Lifeform:'
            
            self.label_scientific_name = Label(master)
            self.label_common_name = Label(master)
            self.label_elevation = Label(master)
            self.label_lifeform = Label(master)
            
            self.label_scientific_name_var = StringVar()
            self.label_common_name_var = StringVar()
            self.label_elevation_var = StringVar()
            self.label_lifeform_var = StringVar()
            
            self.label_scientific_name['textvariable'] = self.label_scientific_name_var
            self.label_common_name['textvariable'] = self.label_common_name_var
            self.label_elevation['textvariable'] = self.label_elevation_var
            self.label_lifeform['textvariable'] = self.label_lifeform_var
            
            self.view()
            
        
        def view(self):
            ''' Apply widgets to the top frame of species frame '''
        
            self.label_scientific_name_label.grid(  row=0, column=0, sticky=W)
            self.label_common_name_label.grid(      row=1, column=0, sticky=W)
            self.label_elevation_label.grid(        row=2, column=0, sticky=W)
            self.label_lifeform_label.grid(         row=3, column=0, sticky=W)
            
            self.label_scientific_name.grid(        row=0, column=1, sticky=W)
            self.label_common_name.grid(            row=1, column=1, sticky=W)
            self.label_elevation.grid(              row=2, column=1, sticky=W)
            self.label_lifeform.grid(               row=3, column=1, sticky=W)
            
            
            
            
    class SpeciesBottomFrame():
        ''' Species bottom frame '''
    
        def __init__(self, master, interface, owner):
            ''' Initialize the bottom frame of the species frame '''
        
            self.interface = interface
            
            self.frame = Frame(master)
            self.make_frame(self.frame)
            self.frame.pack()
            
            
        def make_frame(self, master):
            ''' Create widgets for bottom frame of species frame '''
        
            self.test   # blank line, TODO: implement bottom frame (listbox)