CREATE TABLE recipes(
       'rname' TEXT NOT NULL,
       'rating' INTEGER NOT NULL,
       'difficulty_level' TEXT NOT NULL,
       'type' TEXT NOT NULL,
       'prep_time' TIME NOT NULL,
       'main_ingredients' TEXT NOT NULL,
       'last_made' DATE,
       'details_link' TEXT NOT NULL
);
