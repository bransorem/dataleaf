# ====================================================
# Author: Brannen Sorem ==============================
# Date Created: 05-09-11 =============================
# ====================================================
# Modified: 05-10-11 =================================
# ====================================================

from tkinter import *
from subject import Subject

# ============================================================
# ================ Search Frame ==============================
# ============================================================
class SearchFrame():
    ''' Search frame '''

    def __init__(self, master, interface):
        ''' Initialize search frame '''
    
        self.frame = Frame(master, padx=10, pady=10)
        self.frame.pack()
        
        self.interface = interface
        self.top = self.SearchTopFrame(self.frame, interface, self)
        self.bottom = self.SearchBottomFrame(self.frame, interface, self)
        
        
    def clear_all(self):
        ''' Clear the form and results '''
    
        self.interface.search.species = []
        self.interface.search.observations = []
        self.bottom.left.listbox_species.delete(0, END)
        self.bottom.right.listbox_observations.delete(0, END)
        self.top.entry_species_var.set('')
        self.top.entry_genus_var.set('')
        self.top.entry_observer_first_name_var.set('')
        self.top.entry_observer_last_name_var.set('')
        self.top.entry_date_var.set('')
        self.top.entry_latitude_var.set('')
        self.top.entry_longitude_var.set('')
        self.bottom.left.label_species_results_number_var.set('0')
        self.bottom.right.label_observation_results_number_var.set('0')
    
    
    def search_return(self, pointless_var):
        ''' Forward function due to bind requirement '''
        self.search()


    def search(self):
        ''' Execute search '''
        
        s = self.interface.search
        species = self.top.entry_species_var.get()
        genus = self.top.entry_genus_var.get()
        observer_first_name = self.top.entry_observer_first_name_var.get()
        observer_last_name = self.top.entry_observer_last_name_var.get()
        
        self.interface.search.observations = []
        self.bottom.right.listbox_observations.delete(0, END)
        self.bottom.right.label_observation_results_number_var.set('0')

        if genus != None:
            s.specie = species
            s.genus = genus
            s.observer_first_name = observer_first_name
            s.observer_last_name = observer_last_name
            self.interface.search_species()
            
            self.species_list()
            
        else:
            print('Not successful')
            
            
    def set_species(self, number):
        ''' Set species list '''
    
        selected = self.bottom.left.listbox_species.curselection()
        self.interface.subframe.species()
        

    def observation_list(self, specie):
        ''' Set observation list '''
        
        self.interface.search_observations()
        selected = self.bottom.left.listbox_species.curselection()
        self.interface.navigation.button_species.config(state=NORMAL)
        
        if selected != ():
            genus = self.interface.search.species[int(selected[0])].genus
            species = self.interface.search.species[int(selected[0])].species
            self.interface.search.genus = genus
            self.interface.search.specie = species
            self.interface.search_observations()
            self.interface.current_species_var.set(genus + ' ' + species)
            self.interface.current_species = self.interface.search.species[int(selected[0])]
            
        self.observation_list_load()
        
        
    def observation_list_load(self):
        ''' Load observation list into listbox '''
    
        self.bottom.right.listbox_observations.delete(0, END)
        self.interface.search.key = 3
        self.interface.search.sort(self.interface.search.observations)
        self.bottom.right.label_observation_results_number_var.set(str(len(self.interface.search.observations)))
                    
        for e in self.interface.search.observations:
            self.bottom.right.listbox_observations.insert(END, e.subject + '\t\t' + e.author.firstname + ' ' + e.author.lastname)
        

    def species_list(self):
        ''' Load species into listbox '''
    
        self.bottom.left.listbox_species.delete(0, END)
        self.interface.search.sort(self.interface.search.species)
        self.bottom.left.label_species_results_number_var.set(str(len(self.interface.search.species)))
            
        for e in self.interface.search.species:
            temp_name = e.genus + ' ' + e.species
            self.bottom.left.listbox_species.insert(END, e.genus + ' ' + e.species)
                                
    
    def sort_species(self):
        ''' Sort listbox items by species '''
        self.top.menubutton_sort.config(text='Alphabetical by Species')
        self.interface.search.key = 2
        self.species_list()
        
    def sort_genus(self):
        ''' Sort listbox items by genus '''
        self.top.menubutton_sort.config(text='Alphabetical by Genus')
        self.interface.search.key = 1
        self.species_list()
        
    def sort_observer(self):
        ''' Set listbox items by observer '''
        self.top.menubutton_sort.config(text='Alphabetical by Observer')
        # make sure there has been a search first
        if self.interface.search.species != []:
            self.interface.search.key = 3
            self.observation_list(1)































    class SearchTopFrame():
    
        def __init__(self, master, interface, owner):
        
            self.interface = interface
            self.master = owner            

            self.frame = Frame(master)
            self.make_frame(self.frame)
            self.frame.pack()
        
        
        def make_frame(self, master):
            # Labels
            self.label_genus = Label(master)
            self.label_genus['text'] = 'Genus'
            self.label_species = Label(master)
            self.label_species['text'] = 'Species'
            self.label_observer_first_name = Label(master)
            self.label_observer_first_name['text'] = 'First Name'
            self.label_observer_last_name = Label(master)
            self.label_observer_last_name['text'] = 'Last Name'
            self.label_date = Label(master)
            self.label_date['text'] = 'Date'
            self.label_latitude = Label(master)
            self.label_latitude['text'] = 'Latitude'
            self.label_longitude = Label(master)
            self.label_longitude['text'] = 'Longitude'
            
            self.label_sort = Label(master)
            self.label_sort['text'] = 'Sorting Options:'
            
            # Buttons
            self.button_clear_all = Button(master)
            self.button_clear_all['text'] = 'Clear All'
            self.button_clear_all['command'] = self.master.clear_all
            
            self.button_search = Button(master)
            self.button_search['text'] = 'Search'
            self.button_search['command'] = self.master.search
            
            
            # Entries
            self.entry_genus_var = StringVar()
            self.entry_species_var = StringVar()
            self.entry_observer_first_name_var = StringVar()
            self.entry_observer_last_name_var = StringVar()
            self.entry_date_var = StringVar()
            self.entry_latitude_var = StringVar()
            self.entry_longitude_var = StringVar()
            
            self.entry_genus = Entry(master, textvariable=self.entry_genus_var)
            self.entry_genus['width'] = 30
            self.entry_species = Entry(master, textvariable=self.entry_species_var)
            #self.entry_species['width'] = 30
            self.entry_observer_first_name = Entry(master, textvariable=self.entry_observer_first_name_var)
            self.entry_observer_first_name['width'] = 10
            self.entry_observer_last_name = Entry(master, textvariable=self.entry_observer_last_name_var)
            self.entry_observer_last_name['width'] = 10
            self.entry_date = Entry(master, textvariable=self.entry_date_var)
            self.entry_latitude = Entry(master, textvariable=self.entry_latitude_var)
            self.entry_latitude['width'] = 10
            self.entry_longitude = Entry(master, textvariable=self.entry_longitude_var)
            self.entry_longitude['width'] = 10
            
            
            # Menubuttons
            self.menubutton_sort = Menubutton(master, relief=RAISED, text='Alphabetical by Species', width=25)
            
            self.menubutton_sort.menu = Menu(self.menubutton_sort, tearoff=0)
            self.menubutton_sort['menu'] = self.menubutton_sort.menu
    
            self.menubutton_sort.menu.add_command(label='Alphabetical by Species', command=self.master.sort_species)
            self.menubutton_sort.menu.add_command(label='Alphabetical by Genus', command=self.master.sort_genus)
            self.menubutton_sort.menu.add_command(label='Alphabetical by Observer', command=self.master.sort_observer)
            # Location
            # Date

            
            self.view()
            
            
        def view(self):
            
            self.label_genus.grid(                      row=0, column=3, sticky=W)
            self.label_species.grid(                    row=0, column=6, sticky=W)
            self.label_observer_first_name.grid(        row=1, column=3, sticky=W, columnspan=2)
            self.label_observer_last_name.grid(         row=1, column=6, sticky=W, columnspan=2)
            self.label_date.grid(                       row=2, column=6, sticky=W)
            self.label_latitude.grid(                   row=3, column=1, sticky=W)
            self.label_longitude.grid(                  row=3, column=3, sticky=W)
            
            self.label_sort.grid(                       row=4, column=3, sticky=W)
                
            self.button_clear_all.grid(                 row=3, column=5, sticky=E)
            self.button_search.grid(                    row=3, column=6, sticky=W)
            
            self.entry_genus.grid(                      row=0, column=0, sticky=W+E, columnspan=3)
            self.entry_species.grid(                    row=0, column=4, sticky=W+E, columnspan=2)
            self.entry_observer_first_name.grid(        row=1, column=0, sticky=W+E, columnspan=3)
            self.entry_observer_last_name.grid(         row=1, column=4, sticky=W+E, columnspan=2)
            self.entry_date.grid(                       row=2, column=0, sticky=W+E, columnspan=6)
            self.entry_latitude.grid(                   row=3, column=0, sticky=W)
            self.entry_longitude.grid(                  row=3, column=2, sticky=W)
            
            self.entry_genus.bind(              '<Return>', self.master.search_return)
            self.entry_species.bind(            '<Return>', self.master.search_return)
            self.entry_observer_first_name.bind('<Return>', self.master.search_return)
            self.entry_observer_last_name.bind( '<Return>', self.master.search_return)
            self.entry_date.bind(               '<Return>', self.master.search_return)
            self.entry_latitude.bind(           '<Return>', self.master.search_return)
            self.entry_longitude.bind(          '<Return>', self.master.search_return)
            
            self.menubutton_sort.grid(  row=4, column=5, sticky=W, columnspan=2)
            



















    class SearchBottomFrame():
    
        def __init__(self, master, interface, owner):
        
            self.interface = interface
            self.master = owner

            self.frame = Frame(master)
            self.frame.pack()
            
            self.left = self.LeftFrame(self.frame, interface, self)
            self.right = self.RightFrame(self.frame, interface, self)
            
            
        class LeftFrame():
        
            def __init__(self, master, interface, owner):
            
                self.interface = interface
                self.master = owner
                
                self.frame = Frame(master)
                self.make_frame(self.frame)
                self.frame.pack(side=LEFT)
                
                
                
            def make_frame(self, master):
        
                # Labels
                self.label_species_results = Label(master)
                self.label_species_results['text'] = 'Species Results:'
                self.label_species_results_number_var = StringVar()
                self.label_species_results_number = Label(master)
                self.label_species_results_number['textvariable'] = self.label_species_results_number_var
                self.label_species_results_number_var.set('0')
                
                self.listbox_species = Listbox(master, selectmode=BROWSE, width=30)
                self.listbox_species.bind('<ButtonRelease-1>', self.master.master.observation_list)
                self.listbox_species.bind('<Double-Button-1>', self.master.master.set_species)     # acts like triple click, button release needs to act before selected
                
                self.view()
                
                
            def view(self):
        
                self.label_species_results_number.grid(     row=0, column=1, sticky=W)
                self.label_species_results.grid(            row=0, column=0, sticky=W)

                self.listbox_species.grid(                  row=1, column=0, sticky=W, columnspan=2)
            
            

                
        class RightFrame():
        
            def __init__(self, master, interface, owner):
            
                self.interface = interface
                self.master = owner
                
                self.frame = Frame(master)
                self.make_frame(self.frame)
                self.frame.pack(side=RIGHT)
            
            
            def make_frame(self, master):
            
                # Labels

                self.label_observation_results = Label(master)
                self.label_observation_results['text'] = 'Observation Results:'
                self.label_observation_results_number_var = StringVar()
                self.label_observation_results_number = Label(master)
                self.label_observation_results_number['textvariable'] = self.label_observation_results_number_var
                self.label_observation_results_number_var.set('0')
                
                self.listbox_observations = Listbox(master, selectmode=BROWSE, width=42)
                self.listbox_observations.bind('<ButtonRelease-1>', self.master.master.set_species)
                
                self.view()
                
                
            def view(self):
                
                self.label_observation_results.grid(        row=0, column=0, sticky=W, padx=10)
                self.label_observation_results_number.grid( row=0, column=1, sticky=W, padx=10)
                
                self.listbox_observations.grid(             row=1, column=0, sticky=W, padx=10, columnspan=2)






