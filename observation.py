# ====================================================
# Author: Brannen Sorem ==============================
# Date Created: 05-09-11 =============================
# ====================================================
# Modified: 05-10-11 =================================
# ====================================================

from location import Location
from subject import Subject
from user import User

class Observation():
    ''' Observation class '''
        
    def __init__(self, subject='', author=User(), location=Location(), quantity=0, notes=''):
        ''' Initialize observation object, default to empty '''
        
        self.subject = subject
        self.author = author
        self.location = location
        self.quantity = quantity
        self.notes = notes
        self.location = location

	# Setter methods
    def setsubject(self, subject):
        ''' Set subject '''
        self.subject = subject
    def setauthor(self, author):
        ''' Set author '''
        self.author = author
    def setlocation(self, location):
        ''' Set location '''
        self.location = location
    def setquantity(self, quantity):
        ''' Set quantity '''
        self.quantity = quantity
    def setnotes(self, notes):
        ''' Set notes '''
        self.notes = notes
		
	
