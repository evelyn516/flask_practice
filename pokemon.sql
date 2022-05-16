DROP TABLE IF EXISTS pokemon;
CREATE TABLE pokemon (
    id integer PRIMARY KEY autoincrement,
    name varchar(30) NOT NULL,
    type varchar(20),
    level integer
);

