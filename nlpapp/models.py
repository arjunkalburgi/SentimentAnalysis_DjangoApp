from django.db import models
import nlpapp.sentiment_mod as s

# Create your models here.
class Sentiment(models.Model): 
	"""

	"""

	text = " "

	# function that receives text and spits out pos or neg
	def analysis(self, text):
		if s.sentiment(text)[0] is 'n': 
			self.text = "negative"

		elif s.sentiment(text)[0] is 'p': 
			self.text = "positive"

		else: 
			self.text = " "




	def __str__(self):
		return self.text
