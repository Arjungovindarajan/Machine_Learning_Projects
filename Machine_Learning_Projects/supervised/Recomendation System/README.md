Recomendation system ML project

Types of Recomendation sys
1. content based
	-it have #tags based on the content will recomend (eg. Youtube)
2. colabrative filter
	-User behavioral(intrest) based, A & B persion same rating will recomend each persons (eg. Facebook)
3. Hibrid
	-content based and colabrative filter mixed model (big companys uses)

im taking Movie Recomendation system project 
_content based_ 

steps:

import needed packages,
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
load the data [movie & credits]
movie dataframe have null values but nessasary columns have [no null] values it is satisfied.
credits dataframe no null values in this columns so satisfied with the data.
Both dataframe have common column **"title"** merge both dataframes heare it will be easy to perform
i taking only necessary columns for my final data frame
Data Pre-Processing semi-structure data to change structured data

I have an issue this list all are "string"
TypeError: string indices must be integers im using ast_literal_eval function
to avoid the error **import ast** the package.

new_df['tags'] column each words with dimention like XY graph 5000 vector lines are their. so each close vectors will recomended.

this is the vector shapes
assume xy range apply the (1494, 5000) points.

![plot](.\Recomendation System\source\img1.png)
<p align="center">
  <img src=".\Recomendation System\source\img1.png" width="350" title="img1">
</p>

in the array have tags (words) and some numerical, alfa numerical terms are there.
plural, present, past, future words are there will take nuteral and combined common words the process called steming.
import nltk package

ML model creating

two types of distance are there
cosine distance
uclident distance
cosine distance will take here, it mean total 5000 vactor tages are there nearest angle tags will be recomended.
uclident distance not a proper value so im not take this.

![plot](.\Recomendation System\source\img2.png)
<p align="center">
  <img src=".\Recomendation System\source\img2.png" width="350" title="img2">
</p>

sklearn package have **cosine simalarity** import

pass the vector in the function
vector mean each stemed words

similarity have Index issue on single movie. for example '0' index movie similar movies have no indexs. im using enumerate function here

then shorting and make a list

create function for similar distance movie recomender


#######deployment#######

python -m venv env
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt



git notes

…or create a new repository on the command line

echo "# Machine_Learning_Projects" >> README.md
  git init
  git add README.md
  git commit -m "first commit"
  git branch -M main
  git remote add origin https://github.com/Arjungovindarajan/Machine_Learning_Projects.git
  git push -u origin main

…or push an existing repository from the command line

git remote add origin https://github.com/Arjungovindarajan/Machine_Learning_Projects.git
  git branch -M main
  git push -u origin main

