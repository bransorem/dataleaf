# ====================================================
# Author: Brannen Sorem ==============================
# Date Created: 05-09-11 =============================
# ====================================================
# Modified: 05-09-11 =================================
# ====================================================

class Subject():
    
    def __init__(self, family='', genus='', species='', common_name='', lifeform='', range_low=0, range_high=0):
        ''' Initialize subject '''
        
        self.family = family
        self.genus = genus
        self.species = species
        self.common_name = common_name
        self.lifeform = lifeform
        self.range_low = range_low
        self.range_high = range_high
        
    def setfamily(self, family):
        ''' Set family '''
        self.family = family
    def setgenus(self, genus):
        ''' Set genus '''
        self.genus = genus
    def setspecies(self, species):
        ''' Set species '''
        self.species = species
    def setcommonname(self, common_name):
        ''' Set common name '''
        self.common_name = common_name
    def setlifeform(self, lifeform):
        ''' Set lifeform '''
        self.lifeform = lifeform
    def setrangelow(self, range_low):
        ''' Set range low '''
        self.range_low = range_low
    def setrangehigh(self, range_high):
        ''' Set range high '''
        self.range_high = range_high