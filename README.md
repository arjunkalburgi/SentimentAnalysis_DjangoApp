# SentimentAnalysis_DjangoApp

1. Introduction - what is this?
2. Run it
3. Additional Information

Introduction: 

This app was meant to be an introduction to Django, Natural Language Processing 
and Machine Learning, as well as an expansion to my knowledge of MVC. It's a 
simple app that only does one thing - it takes in text input from the user, puts
the text through the sentiment analysis algorithm, and displays the answer back 
to the user. 



Run it: 

As it is a Dango app, in the working directory run: 
########$ python manage.py runserver
then go to localhost:8000. On the website there are three pages, the MVC and NLP
pages just have text explaining what I learned about the topics and how, the Home 
page has the application explained in the Introduction. You might want to check 
the Additional Information section before trying to run the application.



Additional Information: 

a. sentiment_mod.py
This file was creating with the help of a YouTube tutorial by Sentdex. 
https://www.youtube.com/watch?v=FLZvOKSCkxY&list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL
If you look at the code, a lot of the data is taken from pickled files which are  
not included in the repo because the files are too large (as per GITHUB's requirement) 
Instructions on how to create the pickled files is below.


b. pickling 
There is another file included in the top-level of the repo called createpickles.py
If you run that file in your python shell: 
########$ python createpickles
it should create all the pickled algorithms for you in a folder called "pickled_algos". 
You then need to move this folder into the "/nlpapp/" directory. Then the app should work. 

