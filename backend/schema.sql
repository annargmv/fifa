DROP TABLE IF EXISTS player;

CREATE TABLE player (
  id INTEGER PRIMARY KEY  NOT NULL,
  name TEXT NOT NULL,
  age TEXT NOT NULL,
  photo TEXT NOT NULL,
  nationality TEXT NOT NULL,
  overall integer NOT NULL,
  club TEXT NOT NULL,
  wage TEXT NOT NULL
);