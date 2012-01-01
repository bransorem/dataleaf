# ====================================================
# Author: Brannen Sorem ==============================
# Date Created: 05-09-11 =============================
# ====================================================
# Modified: 05-09-11 =================================
# ====================================================

from tkinter import *

# ====================================================
# ============== Login Frame =========================
# ====================================================


class LoginFrame():
    ''' Manage login widgets '''
    
    def __init__(self, master, interface):
        ''' Creates a frame for the login widgits '''
        
        login_frame = Frame(master, padx=10, pady=10)
        self.make_frame(login_frame)
        login_frame.pack(side=RIGHT)
        
        self.interface = interface
                
        
    def make_frame(self, master):
        ''' Build login frame widgets '''
        
        # Login button
        self.button_login = Button(master)
        self.button_login['text'] = 'login'
        self.button_login['command'] = self.login
        
        # Labels
        self.strv = StringVar()
        self.strv.set('User: guest')
        
        self.label_user = Label(master)
        self.label_user['text'] = 'User: '
        self.label_password = Label(master)
        self.label_password['text'] = 'Password: '
        self.label = Label(master)
        self.label['textvariable'] = self.strv
        
        # Entry boxes
        self.entry_user_var = StringVar()
        self.entry_password_var = StringVar()
        self.entry_user = Entry(master, textvariable=self.entry_user_var)
        self.entry_user['width'] = 15
        self.entry_password = Entry(master, textvariable=self.entry_password_var, show='*')
        self.entry_password['width'] = 15
        
        self.entry_password.bind('<Return>', self.login_binding)
        self.entry_user.bind('<Return>', self.login_binding)
        
        # Element layout
        self.view()


    def view(self):
        ''' Layout login widgets '''
        
        self.label_user.grid(row=0, column=0)
        self.entry_user.grid(row=0, column=1)
        self.label_password.grid(row=0, column=2)
        self.entry_password.grid(row=0, column=3)
        self.button_login.grid(row=1, column=3)
        self.label.grid(row=1, column=1)

        
    def login_binding(self, binding):
        ''' For redirect due to bind handling '''
        self.login()
        
    def login(self):
        ''' Query db for user and set as current user '''
                
        u = self.interface.user
        user = self.entry_user_var.get()
        password = self.entry_password_var.get()
        
        # for now, just check that user and pass aren't empty
        # TODO  make each have validation with feedback
        if (user and password) != '':
            u.alias = user
            u.password = password
            self.interface.login()
            self.strv.set('User: ' + u.alias)
            #self.button_login['text'] = 'logout' 
            self.entry_user_var.set('')
            self.entry_password_var.set('')
            self.interface.navigation.button_new_observation.config(state=NORMAL)
        else:
            u.reset()
            self.strv.set('User: ' + u.alias)
            self.interface.navigation.button_new_observation.config(state=DISABLED)
            #self.button_login['text'] = 'login'
            
