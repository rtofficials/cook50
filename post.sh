#!/bin/bash

curl "http://localhost:5000/add_recipe" -d "rname=Chicken Parmesian&rating=6&difficulty_level=5&type=Dinner&prep_time=00:30:00&main_ingredients=chiken, salt, spices&last_made=2021-07-22&details_link=https://www.somerecipesite.com/chiken parmesian";

curl "http://localhost:5000/add_recipe" -d "rname=Kadhai Paneer&rating=9&difficulty_level=8&type=Dinner&prep_time=00:40:00&main_ingredients=Paneer, Kadhai, salt, water, butter,Cashew Nuts&last_made=2021-05-18&details_link=https://www.somerecipesite.com/kadhai-paneer"; 
