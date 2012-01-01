# ====================================================
# Author: Brannen Sorem ==============================
# Date Created: 05-09-11 =============================
# ====================================================
# Modified: 05-10-11 =================================
# ====================================================

class User():
   
    def __init__(self, firstname='', lastname='', alias='guest', title='', website='', email=''):
        ''' Initialize User '''
        
        self.access = 3
        self.firstname = firstname
        self.lastname = lastname
        self.alias = alias
        self.title = title
        self.website = website
        self.email = email
        
        
    def query(self):
        ''' Return the query to execute '''
        
        query = 'SELECT * FROM User WHERE User.alias = "' + self.alias + '" and User.password = "' + self.password + '"'
        return query
        
        
    def set(self, dat):
        ''' Set user info from data sent by database query '''
    
        # If the user exists in the database
        if dat != None:
            self.firstname = dat[1]
            self.lastname = dat[2]
            self.title = dat[5]
            self.website = dat[7]
            self.email = dat[8]
            self.access = dat[4]
        else: self.reset()
        
        
    def reset(self):
        ''' Reset all User fields to '' '''

        self.firstname = self.lastname = self.title = \
        self.password = self.website = self.email = ''
        self.alias = 'guest'
        
        
    def show(self):
        ''' Show all user attributes (mostly for debugging) '''
        
        print(self.firstname)
        print(self.lastname)
        print(self.alias)
        print(self.email)
        print(self.access)
        
        