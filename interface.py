# ====================================================
# Author: Brannen Sorem ==============================
# Date Created: 05-09-11 =============================
# ====================================================
# Modified: 05-09-11 =================================
# ====================================================

from databaseconnection import DatabaseConnection
from user import User
from search import Search


class Interface():
    ''' Singleton class to manage shared components '''

    _instance_ = None
    
    def __init__(self):
        ''' Initialize interface and create singleton instance '''
        
        if Interface._instance_:
            raise Interface._instance_
        Interface._instance_ = self
        
        Interface.user = User()
        Interface.search = Search()
        self.db = DatabaseConnection()
            
        
    def login(self):
        ''' User login, save to interface '''
        
        u = Interface.user
        result = self.db.execute(u.query())
        dat = result.fetchone()
        u.set(dat)
        
        
    def search_species(self):
        ''' Save species to interface '''
    
        s = Interface.search
        result = self.db.execute(s.query())
        dat = result.fetchall()
        s.set_species(dat)
        

    def search_observations(self):
        ''' Save observations to interface '''
    
        s = Interface.search
        result = self.db.execute(s.query_observations())
        dat = result.fetchall()
        s.set_observations(dat)
        