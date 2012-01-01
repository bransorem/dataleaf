# ====================================================
# Author: Brannen Sorem ==============================
# Date Created: 05-09-11 =============================
# ====================================================
# Modified: 05-09-11 =================================
# ====================================================

import sqlite3

class DatabaseConnection():
    ''' Connection to database managed by this class '''
    
    def __init__(self):
        ''' Initialize database connection and set cursor and connection '''
        self.connection = sqlite3.connect('dataleaf.db')
        self.cursor = self.connection.cursor()
        
    def execute(self, query=''):
        ''' Send execute query sent as string '''
        return self.cursor.execute(query)
