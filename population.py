import csv
import sqlite3

datain = csv.reader(open('ABSP-plants.csv'), delimiter=',', quotechar='|')

# put CSV data into a list
lst = []
for row in datain:
    lst.append(row)


# separate scientific name (genus and species)
scinames = []
for sci in lst:
    scinames.append(sci[4])
    tempname = scinames.pop()
    tempname = tempname.split(' ', 2)
    scinames.append(tempname)


# prep variables
famid = {}
genusid = {}
fkey = -1
gkey = -1
family_string = ""
genus_string = ""


# for every element in the list
for i, el in enumerate(lst):    
    el[4] = scinames[i][0]
    el.insert(5, scinames[i][1])
    # add family id
    if el[3] in famid:
        el.insert(10, famid.get(el[3]))
    else:
        fkey += 1
        famid[el[3]] = fkey
        el.insert(10, fkey)
        family_string += el[3] + "," + str(fkey) + "\n"
    # add genus id
    if el[4] in genusid:
        el.insert(11, genusid.get(el[4]))
    else:
        gkey += 1
        genusid[el[4]] = gkey
        el.insert(11, gkey) 
        genus_string += el[4] + "," + str(gkey) + "," + str(el[10]) + "\n"

# replace heading names
lst[0][0] = "quantity"
#lst[0][1] Introduced
#lst[0][2] Rare
lst[0][3] = "family"
lst[0][4] = "genus"
lst[0][5] = "species"
lst[0][6] = "common_name"
lst[0][7] = "lifeform"
lst[0][8] = "range_low"
lst[0][9] = "range_high"
lst[0].insert(10, "fam_id")
lst[0].insert(11, "genus_id")
del lst[0]


subject = []
family = []
genus = []
genusID = []

i = 0


print("Creating subject, family, and genus data…")

for e in lst:

    #  SUBJECT --------------
    temp = []
    temp.append(i)          # sub_id
    temp.append(e[11])      # genus_id
    temp.append(e[5])       # species
    temp.append(e[6])       # common_name
    temp.append(None)       # jepson_link
    temp.append(None)       # photo
    temp.append(e[7])       # lifeform
    temp.append(e[8])       # range_low
    temp.append(e[9])       # range_high
    subject.append(temp)
    i += 1
    
    #  FAMILY ---------------
    temp = []
    temp.append(e[10])      # fam_id
    temp.append(e[3])       # family
    
    if temp not in family:
        family.append(temp)
    
    #  GENUS ----------------
    temp = []   
    temp.append(e[11])      # genus_id
    temp.append(e[10])      # fam_id
    temp.append(e[4])       # genus
    
    if e[11] not in genusID:
        genusID.append(e[11])
        genus.append(temp)



# ==========================================================================
# ========= USERS ==========================================================

print("Creating user data…")

datain = csv.reader(open('dataleaf_users.csv'), delimiter=',', quotechar='|')

# put CSV data into a list
users = []
for row in datain:
    users.append(row)
    
temp = []
temp.append('user_id')
temp.append('first_name')
temp.append('last_name')
temp.append('alias')
temp.append('access')
temp.append('title')
temp.append('password')
temp.append('website')
temp.append('email')

#users.insert(0, temp)





# ==========================================================================
# ========= OBSERVATIONS ===================================================

print("Creating observation data…")

datain = csv.reader(open('ObservationTableData.csv'), delimiter=',', quotechar='|')

# put CSV data into a list
observations = []
i = 0
for row in datain:
    row.insert(0, i)
    observations.append(row)
    i += 1
    
temp = []
temp.append('obs_id')
temp.append('loc_elevation')
temp.append('author')
temp.append('date')
temp.append('subject')
temp.append('loc_description')
temp.append('loc_lat')
temp.append('loc_long')
temp.append('quantity')
temp.append('notes')

#observations.insert(0, temp)



# ==========================================================================
# ========= DATABASE =======================================================



            
conn = sqlite3.connect("dataleaf.db")
c = conn.cursor()


# Doesn't work yet - can only execute one statement at a time
reset_database = open('db.sql', 'r').read()
c.executescript(reset_database)


print("Writing subject data into Subject table…")
for sub in subject:    
    c.execute("INSERT INTO Subject values (?, ?, ?, ?, ?, ?, ?, ?, ?);", sub)
    
    
    
print("Writing observations data into Observation table…")
for obs in observations:    
    c.execute("INSERT INTO Observation values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", obs)
    
    
    
print("Writing family data into Family table…")
for fam in family:    
    c.execute("INSERT INTO Family values (?, ?);", fam)
    
    
    
print("Writing user data into User table…")
for u in users:    
    c.execute("INSERT INTO User values (?, ?, ?, ?, ?, ?, ?, ?, ?);", u)
    
    
    
print("Writing genus data into Genus table…")
for gen in genus:    
    c.execute("INSERT INTO Genus values (?, ?, ?);", gen)
    
    

    
    


'''
test = c.execute('SELECT * FROM Subject')
print(test.fetchone())

test = c.execute('SELECT * FROM Observation')
print(test.fetchone()[4])

test = c.execute('SELECT * FROM Family')
print(test.fetchone())

test = c.execute('SELECT * FROM User')
print(test.fetchone()[8])

test = c.execute('SELECT * FROM Genus')
print(test.fetchone())
'''



conn.commit()

conn.close()