from django.shortcuts import render


def index(request):
	template = 'main/index.html'
	return render(request, template)
	
def target1(request):
	template = 'main/target1.html'
	return render(request, template)

def actual1(request):
	template = 'main/actual1.html'
	return render(request, template)
	
def class2(request):
	template = 'main/class2.html'
	return render(request, template)
	
def risk2(request):
	template = 'main/risk2.html'
	return render(request, template)
	
def tech3(request):
	template = 'main/tech3.html'
	return render(request, template)
	
def org3(request):
	template = 'main/org3.html'
	return render(request, template)

def regular4(request):
	template = 'main/regular4.html'
	return render(request, template)

def incident4(request):
	template = 'main/incident4.html'
	return render(request, template)

def rez5(request):
	template = 'main/rez5.html'
	return render(request, template)

def grow5(request):
	template = 'main/grow5.html'
	return render(request, template)

def templ(request):
	template = 'main/templ.html'
	return render(request, template)

def cheme(request):
	template = 'main/cheme.html'
	return render(request, template)

def termin(request):
	template = 'main/termin.html'
	return render(request, template)

