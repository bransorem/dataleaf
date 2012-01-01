# ====================================================
# Author: Brannen Sorem ==============================
# Date Created: 05-09-11 =============================
# ====================================================
# Modified: 05-10-11 =================================
# ====================================================

class Location():
    ''' Location object '''
	
    def __init__(self, latitude=0, longitude=0, elevation=0, description=''):
       ''' Initialize Location object '''
       self.latitude = latitude
       self.longitude = longitude
       self.elevation = elevation
       self.description = description
	
    def setlatitude(self, latitude):
        ''' Set latitude '''
        self.latitude = latitude
    def setlongitude(self, longitude):
        ''' Set longitude '''
        self.longitude = longitude
    def setelevation(self, elevation):
        ''' Set elevation '''
        self.elevation = elevation
    def setdescription(self, description):
        ''' Set description '''
        self.description = description
		

