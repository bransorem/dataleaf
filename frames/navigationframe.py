# ====================================================
# Author: Brannen Sorem ==============================
# Date Created: 05-09-11 =============================
# ====================================================
# Modified: 05-09-11 =================================
# ====================================================

from tkinter import *
from .searchframe import *
from .speciesframe import *


# ============================================================
# =============== Navigation Frame ===========================
# ============================================================
class NavigationFrame():
    ''' Manage navigation frame '''
    
    def __init__(self, master, interface):
        ''' Initialize navigation frame, create subframe (managed by Interface) '''
    
        interface.navigation = self
        self.interface = interface
        
        frame = Frame(master, padx=10, pady=10)
        self.make_frame(frame)
        frame.pack()
        
        self.frame = frame
        self.master = master
        
        self.interface.subframe = self
        self.subframe  = SearchFrame(master, self.interface)
        
        
    def make_frame(self, master):
        ''' Create widgets for navigation '''
        
        # Search button
        self.button_search = Button(master, state=DISABLED)
        self.button_search['text'] = 'Search'
        self.button_search['command'] = self.search
        
        # Species button
        self.button_species = Button(master)
        self.button_species['text'] = 'Species'
        self.button_species['command'] = self.species
        
        # Observation button
        self.button_observation = Button(master)
        self.button_observation['text'] = 'Observation'
        self.button_observation['command'] = self.observation
        
        # New Observation button
        self.button_new_observation = Button(master, state=DISABLED)
        self.button_new_observation['text'] = 'New Observation'
        self.button_new_observation['command'] = self.new_observation
        
        self.view()
        
        
    def view(self):
        ''' Add widgets to frame '''
    
        self.button_search.grid(row=0, column=0)
        self.button_species.grid(row=0, column=1)
        self.button_observation.grid(row=0, column=2)
        self.button_new_observation.grid(row=0, column=3)
        
        
    def search(self):
        ''' Search button clicked, set that as subframe '''
        
        self.subframe.frame.pack_forget()
        self.subframe = SearchFrame(self.master, self.interface)
        # Remember state of species/observations lists
        self.subframe.species_list()
        self.subframe.observation_list_load()
        
        # Highlight current tab
        self.button_search.config(state=DISABLED)
        self.button_species.config(state=NORMAL)
        self.button_observation.config(state=NORMAL)
        #self.button_new_observation.config(state=NORMAL)
        
        
    def species(self):
        ''' Species button clicked, set that as subframe '''
        
        self.subframe.frame.pack_forget()
        self.subframe = SpeciesFrame(self.master, self.interface)
        
        # Highlight current tab
        self.button_search.config(state=NORMAL)
        self.button_species.config(state=DISABLED)
        self.button_observation.config(state=NORMAL)
        #self.button_new_observation.config(state=NORMAL)
        
        
    def observation(self):
        ''' Observation button clicked, set that as subframe '''
        
        self.subframe.frame.pack_forget()
        #self.subframe = ObservationFrame(self.master, self.interface)
        
        # Highlight current tab
        self.button_search.config(state=NORMAL)
        self.button_species.config(state=NORMAL)
        self.button_observation.config(state=DISABLED)
        #self.button_new_observation.config(state=NORMAL)
        
        
    def new_observation(self):
        ''' New Observation button clicked, set that as subframe '''
        
        self.subframe.frame.pack_forget()
        #self.subframe = NewObservationFrame(self.master, self.interface)
        
        # Highlight current tab
        self.button_search.config(state=NORMAL)
        self.button_species.config(state=NORMAL)
        self.button_observation.config(state=NORMAL)
        #self.button_new_observation.config(state=DISABLED)
        
        
