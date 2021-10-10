

CREATE_TABLE_CHARACTERS = """CREATE TABLE IF NOT EXISTS characters (" 
                                 id INTEGER, name VARCHAR(255), 
                                 description TEXT, 
                                 modified TIMESTAMP,
                                 PRIMARY KEY(id)
                           )"""
CREATE_TABLE_COMICS = """CREATE TABLE IF NOT EXISTS comics (" 
                             id INTEGER,  
                             digital_id INTEGER,
                             character_id INTEGER,
                             title TEXT, 
                             issue_number INTEGER,  
                             variantDescription TEXT, 
                             description TEXT,
                             modified TIMESTAMP,
                             isbn CHARACTER(255),
                             upc CHARACTER(255),
                             diamondCode CHARACTER(255),
                             ean CHARACTER(255),
                             issn CHARACTER(255),
                             format CHARACTER(255),
                             pageCount INTEGER,
                             PRIMARY KEY (id),
                             CONSTRAINT fk_charecter FOREIGN KEY(character_id) REFERENCES characters(id)
                             )"""

INSERT_INTO_CHARACTERS = """INSERT INTO characters VALUES (%s, %s, %s, %s)"""
INSERT_INTO_COMICS = """INSERT INTO comics VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""