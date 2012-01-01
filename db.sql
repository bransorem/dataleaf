DROP TABLE IF EXISTS User;
CREATE TABLE User (
 usr_id         INTEGER     PRIMARY KEY,
 first_name     TEXT,
 last_name      TEXT        NOT NULL,
 alias          TEXT        NOT NULL,
 access         INTEGER     NOT NULL,
 title          TEXT,
 password       TEXT        NOT NULL,
 website        TEXT,
 email          TEXT
);

DROP TABLE IF EXISTS Family;
CREATE TABLE Family (
 fam_id         INTEGER     NOT NULL  PRIMARY KEY,
 family         TEXT        NOT NULL
);

DROP TABLE IF EXISTS Genus;
CREATE TABLE Genus (
 genus_id       INTEGER     NOT NULL  PRIMARY KEY,
 fam_id         INTEGER     NOT NULL,
 genus          TEXT        NOT NULL,
 FOREIGN KEY (fam_id) REFERENCES Family(fam_id)
);

DROP TABLE IF EXISTS Subject;
CREATE TABLE Subject (
 sub_id         INTEGER     NOT NULL  PRIMARY KEY,
 genus_id       INTEGER     NOT NULL,
 species        TEXT        NOT NULL,
 common_name    TEXT        NOT NULL,
 jepson_link    TEXT,
 photo          BLOB,
 lifeform       TEXT        NOT NULL,
 range_low      INTEGER     NOT NULL,
 range_high     INTEGER     NOT NULL,
 FOREIGN KEY (genus_id) REFERENCES Genus(genus_id)
);

DROP TABLE IF EXISTS Observation;
CREATE TABLE Observation (
 obs_id         INTEGER     NOT NULL  PRIMARY KEY,
 loc_elevation  INTEGER,
 author         INTEGER     NOT NULL,
 date           TEXT        NOT NULL,
 subject        INTEGER     NOT NULL,
 loc_description TEXT,
 loc_lat        REAL,
 loc_long       REAL,
 quantity       INTEGER     NOT NULL,
 notes          TEXT,
 FOREIGN KEY (author) REFERENCES User(usr_id),
 FOREIGN KEY (subject) REFERENCES Subject(sub_id)
);

