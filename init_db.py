import sqlite3

connection = sqlite3.connect('pokemon.db')


with open('pokemon.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO pokemon (name, type, level) VALUES (?, ?, ?)",
            ('Pikachu', 'electric', 16)
            )

cur.execute("INSERT INTO pokemon (name, type, level) VALUES (?, ?, ?)",
            ('Magikarp', 'water', 88)
            )

cur.execute("INSERT INTO pokemon (name, type, level) VALUES (?, ?, ?)",
            ('Psyduck', 'psychic', 34)
            )

connection.commit()
connection.close()




'''

INSERT INTO pokemon (name, type, level)
VALUES 
    ('Pikachu', 'electric', 16)
    ('Magikarp', 'water', 88)
    ('Psyduck', 'psychic', 34)

'''
