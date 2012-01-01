# ====================================================
# Author: Brannen Sorem ==============================
# Date Created: 05-09-11 =============================
# ====================================================
# Modified: 05-10-11 =================================
# ====================================================

from operator import itemgetter
from subject import Subject
from observation import Observation
from location import Location
from user import User

class Search():
    ''' Search object, where the magic happens '''

    def __init__(self):
        ''' Initialize search object '''
        
        self.genus = None
        self.specie = None
        self.observer_first_name = None
        self.observer_last_name = None
        self.species = []
        self.observations = []
        self.key = 2
        self.key_observer = 1
        
        
    def query(self):
        ''' Return the query to execute '''
        
        query  = 'SELECT family, genus, species, common_name, lifeform, range_low, range_high '
        query += 'FROM Subject, Genus, Family '
        query += 'WHERE Subject.sub_id = Genus.genus_id and Family.fam_id = Genus.fam_id'
        observer_query  = 'SELECT family, genus, species, common_name, lifeform, range_low, range_high, first_name, last_name '
        observer_query += 'FROM User, Observation, Subject, Genus, Family '
        observer_query += 'WHERE Subject.sub_id = Genus.genus_id and Observation.author = User.usr_id and Observation.subject = Subject.sub_id and Family.fam_id = Genus.fam_id'

        
        if self.observer_first_name != '':
            observer_query += ' AND User.first_name="' + self.observer_first_name + '"'
            query = observer_query
        if self.observer_last_name != '':
            observer_query += ' AND User.last_name="' + self.observer_last_name + '"'
            query = observer_query
        if self.genus != '':
            query += ' AND Genus.genus="' + self.genus + '"'
        if self.specie != '':
            query += ' AND Subject.species="' + self.specie + '"'
            
        return query
                
        
    def query_observations(self):
        ''' Return the query to execute '''
        
        query  = 'SELECT genus, species, first_name, last_name, date, quantity, notes, loc_lat, loc_long, loc_elevation, loc_description, title, website, email '
        query += 'FROM Subject, Genus, Observation, User '
        query += 'WHERE Subject.sub_id = Genus.genus_id and Subject.sub_id = Observation.subject and User.usr_id = Observation.author'
        
        if self.genus != '' and self.genus != None:
            query += ' AND Genus.genus="' + self.genus + '"'
        if self.specie != '' and self.specie != None:
            query += ' AND Subject.species="' + self.specie + '"'
        if self.observer_first_name != '' and self.observer_first_name != None:
            query += ' AND User.first_name="' + self.observer_first_name + '"'
        if self.observer_last_name != '' and self.observer_last_name != None:
            query += ' AND User.last_name="' + self.observer_last_name + '"'
            
        return query
        
        
    def set_species(self, dat):
        ''' Set the species list '''
    
        if dat != None:
            self.species = []
            dat.sort(key=itemgetter(self.key))
            
            temp_set = set()        # to avoid duplicates from observations
            for e in dat:
                temp_name = e[1] + e[2]
                subject = Subject(e[0], e[1], e[2], e[3], e[4], e[5], e[6])
                
                if not(temp_name in temp_set):
                    temp_set.add(temp_name)
                    self.species.append(subject)
                
                
    def set_observations(self, dat):
        ''' Set the observations list '''
    
        if dat != None:
            self.observations = []
            dat.sort(key=itemgetter(self.key-1))
            for e in dat:
                author = User(e[2], e[3], e[11], e[12], e[13])
                location = Location(e[7], e[8], e[9], e[10])
                subject = e[0] + ' ' + e[1]
                observation = Observation(subject, author, location, e[5], e[6])
                #self.observations.append(e)
                self.observations.append(observation)


    def sort(self, dat):
        ''' Sort list '''
        
        # Sort by Genus
        if self.key == 1:
            self.species = []   # empty list
            dat.sort(key=lambda x: x.genus)
            
            for e in dat:
                self.species.append(e)
        # Sort by Species
        elif self.key == 2:
            self.species = []   # empty list
            dat.sort(key=lambda x: x.species)
            
            for e in dat:
                self.species.append(e)
        # Sort by Observer
        elif self.key == 3:
            self.observations = []   # empty list
            dat.sort(key=lambda x: x.author.firstname)
            dat.sort(key=lambda x: x.author.lastname)
            
            for e in dat:
                self.observations.append(e)
        
            
            
            
            
            