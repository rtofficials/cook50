CREATE TABLE recipes(
       'rname' TEXT NOT NULL UNIQUE,
       'rating' INTEGER NOT NULL  CHECK (rating<6),
       'difficulty_level' INTEGER NOT NULL,
       'r_type' TEXT NOT NULL,
       'prep_time' TIME NOT NULL,
       'main_ingredients' TEXT NOT NULL,
       'last_made' DATE,
       'details_link' TEXT NOT NULL
);
