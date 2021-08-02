#!/bin/sh

curl "http://127.0.0.1:5000/add_recipe" \
-d "rname=Aaloo Tikki&rating=2&difficulty_level=5&type=Evening Snack&prep_time=00:45:00&main_ingredients=aaloo, oil, curd&last_made=2021-04-10&details_link=https://somerecipesite/aaloo_tikki_for_begineers"
