#!/bin/bash

curl "http://localhost:5000/add_recipe" -d "rname=Chicken Parmesian&rating=6&difficulty_level=5&type=Dinner&prep_time=00:30:00&main_ingredients=chiken, salt, spices&last_made=2021-07-22&details_link=https://www.somerecipesite.com/chiken parmesian";

curl "http://localhost:5000/add_recipe" -d "rname=Kadhai Paneer&rating=9&difficulty_level=8&type=Dinner&prep_time=00:40:00&main_ingredients=Paneer, Kadhai, salt, water, butter,Cashew Nuts&last_made=2021-05-18&details_link=https://www.somerecipesite.com/kadhai-paneer";

curl "http://localhost:5000/add_recipe" -d "rname=Palak Paneer&rating=5&difficulty_level=7&type=Dinner&prep_time=00:50:00&main_ingredients=Palak, paneer, salt, spices&last_made=2021-07-02&details_link=https://www.somerecipesite.com/palak-paneer";


curl "http://localhost:5000/add_recipe" -d "rname=Besan Chile&rating=4&difficulty_level=1&type=breakfast&prep_time=00:15:00&main_ingredients=gram flour, water, salt, red chilli, garam masala, ghee&last_made=2021-06-14&details_link=https://www.somerecipesite.com/besan-chile";


curl "http://localhost:5000/add_recipe" -d "rname=sooji halwa&rating=4&difficulty_level=3&type=sweet dish&prep_time=00:30:00&main_ingredients=semolina(sooji), sugar, water, ghee, dry fruits&last_made=2021-06-08&details_link=https://www.somerecipesite.co    m/sooji-halwa";
