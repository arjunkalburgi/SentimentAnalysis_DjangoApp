from django.shortcuts import render, render_to_response

# Create your views here.
from nlpapp.models import Sentiment
from django.views.generic import ListView

# def home(request): 
# 	return render_to_response("home.html", {"text": " ",
# 											"obj": Sentiment.objects.all()[0],
# 											"title": "Welcome to this simple Sentiment Analysis Application"})
# def senti(request, text): 
# 	searchtext = self.request.GET.get("search_text", "")
# 	print(searchtext)
# 	searchtext = searchtext.strip().lower()
# 	return render_to_response("home.html", {"text": Sentiment.objects.all()[0].analysis(searchtext),
# 											"obj": Sentiment.objects.all()[0],
# 											"title": "Thanks for trying this simple Sentiment Analysis Application"})

def mvc(request): 
	return render_to_response("mvc.html", {"title": "Model, View, Controller"})

def nlu(request): 
	return render_to_response("nlp.html", {"title": "Natural Language Processing"})


class Senty(ListView):
	"""docstring for Senty"""
	model = Sentiment
	context_object_name = "senti"

	def dispatch(self, request, *args, **kwargs):
		return super(Senty, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		#Get the current context.
		context = super(Senty, self).get_context_data(**kwargs)

		search_text = "" # Assume no search
		if self.request.method == "GET": 
			search_text = self.request.GET.get("search_text", "").strip()
			print("1", search_text, type(search_text))

		if search_text != "": 
			# get the result of the analysis 
			a = Sentiment.objects.all()[0]
			a.analysis(search_text)
			analysis_result = a.text
			print("2", analysis_result)
			# analysis_result = [a]
			# print("2", analysis_result[0].text)
		else: 
			analysis_result = []
		print("3", analysis_result)

		# adding items to context for display
		context["search_text"] = search_text
		context["analysis_result"] = analysis_result

		return  context