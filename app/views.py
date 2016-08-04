from django.shortcuts import render, redirect 

from django.http import HttpResponse, HttpResponseRedirect
from app.models import State, City, StateCapital

from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView  
from app.forms import CitySearchForm, CityCreate, EditCity, CreateState, EditState
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def delete_state(request, pk):

	State.objects.get(pk=pk).delete()

	return redirect('/state_list/' )

def create_state(request):

	context ={}

	form = CreateState(request.GET)

	context['form'] = form 

	if form.is_valid():
		form.save()

	return render (request, 'create_state.html', context)

@login_required
def edit_state(request, pk):

	context = {} 

	state = State.objects.get(pk=pk)

	context['state'] = state

	form = EditState(request.POST or None, instance=state)

	context ['form'] = form

	if form.is_valid():
		form.save()

		return redirect('/state_list' )

	return render (request, 'state_edit.html', context)

@login_required
def delete_city(request, pk):

	City.objects.get(pk=pk).delete()

	return redirect('/city_list/' )

@login_required
def edit_city(request, pk):

	context = {} 

	city = City.objects.get(pk=pk)

	context['city'] = city

	form = EditCity(request.POST or None, instance=city)

	context ['form'] = form

	if form.is_valid():
		form.save()

		return redirect('/city_list' )

	return render (request, 'city_edit.html', context)

def create_city(request):

	context ={}

	form = CityCreate(request.GET)

	context['form'] = form 

	if form.is_valid():
		form.save()

	return render (request, 'city_create.html', context)


def city_search_post(request):

	context = {}

	form = CitySearchForm(request.POST)

	context ['form'] = form

	if request.method=='POST':

		if form.is_valid():
			city = form.cleaned_data.get('city', 'Orem')
			state = form.cleaned_data.get('state','Utah')

			context ['cities'] =City.objects.filter(name=city, state__name=state)

	return render (request, 'city_search_post.html', context)


		

	return HttpResponse(request.method)

def city_search(request):

	context = {}

	form = CitySearchForm(request.GET)

	if form.is_valid():
		state = form.cleaned_data.get('state','Utah')
		city = form.cleaned_data.get('city','Orem')
		cities = City.objects.filter(name=city, state__name=state)
		context ['cities'] = cities
		context ['form'] = form
	else:
		context ['form'] = form

	




	return render (request, 'city_search.html', context)

def city_search_old(request):

	context = {}

	form = CitySearchForm(request.GET)

	#print form.data : careful, make sure its clean first

	print form.is_valid()

	print form.cleaned_data

	# state = form.cleaned_data['state']
	# city = form.cleaned_data['city']

	state = form.cleaned_data.get('state','Utah')
	city = form.cleaned_data.get('city','Orem')

	print "%s is a state" % state
	print "%s is a city" % city

	cities = City.objects.filter(name=city, state__name=state)

	context ['cities'] = cities
	context ['form'] = form


	return render (request, 'city_search.html', context)




class StateListView(ListView):
	model = State
	template_name = "state_list.html"
	context_object_name = "states"

class StateDetailView(DetailView):
	model = State 
	template_name = "state_detail.html"
	context_object_name = "state" 

class CityListView(ListView):
	model = City 
	template_name = "city_list.html"
	context_object_name = "cities"

class CityDetailView(DetailView):
	model = City 
	template_name = "city_detail.html"
	context_object_name = "city" 




def statecapital_list(request):
	context = {}

	context['statecapitals'] = StateCapital.objects.all()

	return render (request, 'statecapital_list.html', context)

def statecapital_detail(request, pk):
	context = {}

	statecapital = StateCapital.objects.get(pk=pk)

	context ['statecapital'] = statecapital

	return render (request, 'statecapital_detail.html', context)


def city_detail(request, pk):
	context = {}

	city = City.objects.get(pk=pk)

	context['city'] = city

	return render (request, 'city_detail.html', context)



def city_list(request):
	state_number = request.GET.get('state_number', 46)

	print request.GET

	print state_number

	context = {}

	context ['states'] = State.objects.all() 

	context ['cities'] = City.objects.filter(state__pk=state_number)

	return render (request, 'city_list.html', context)





def state_detail(request, pk):
	context = {}

	state = State.objects.get(pk=pk)

	context ['state'] = state

	return render (request, 'state_detail.html', context)



def stateslist(request):
	context = {}

	states= State.objects.all()

	context ['states'] = states 

	return render (request, 'stateslist.html', context)







def list(request):
	context = {}
	states = State.objects.all()

	context ['states'] = states

	return render (request, 'list.html', context)




def detail(request, pk):
	context = {}

	state = State.objects.get(pk=pk)
	context['state'] = state 

	return render (request, "detail.html", context)













def template_view2(request):
	context= {}
	state_city = {}

	states = State.objects.all()

	for state in states:
		cities = state.city_set.filter(name__startswith='A')

		state.name = { state.name :cities }

		state_city.update(state.name)

	context ['states'] = state_city

	return render(request,'base2.html', context)




def template_view(request):

	context = {}

	states = State.objects.all()

	context['states'] = states 

	return render(request, 'base.html', context)




# class GetPost(view):

# 	def get(self, request, *args, **kwargs):
# 		city_state_string = """
	

# 		<form action="/form_view/" ="POST" >

# 		State: <input type="text" name = "state" >

# 		<br>

# 		City: <input type="text" name= "city" >

# 		<br>

# 		<input type="submit" value="Search" >

# 		</form>

# 		<br>
# 		<br>
# 		""" % ()
# 		return HttpResponse(city_state_string)

# def post(self, request, *args, **kwargs):

# 	get_state = request.POST.get('state', 'N')
#   get_city = request.POST.get('city', 'N')




@csrf_exempt
def form_view(request):

	

	get_state = request.GET.get('state', 'C')
	get_city = request.GET.get('city', 'C')


	city_state_string = """
	POST: %s <br>
	GET: %s <br>
	META: %s <br>


	<form action="/form_view/" method="POST" >

	State: <input type="text" name = "state" >

	<br>

	City: <input type="text" name= "city" >

	<br>

	<input type="submit" value="Search" >

	</form>

	<br>
	<br>
	""" % (escape(request.POST), escape(request.GET), escape(request.META))

	states = State.objects.filter(name__startswith=get_state)

	for state in states:
		cities = state.city_set.filter(name__startswith=get_city)

		for city in cities:
			city_state_string += "<b>%s</b> %s | %s <br>" % (state, city.name, city.zipcode)

	
 
	return HttpResponse(city_state_string)



def get_post(request):

	starts_with = request.GET['state_name'] 

	states = State.objects.filter(name__startswith=starts_with)

	state_string =''

	for state in states:
		state_string += '%s <br>' % state.name

	return HttpResponse(state_string)

def first_view(request):

	states = State.objects.all()
	#	states_list=[]
	text_string = ''

	for state in states:
		cities = state.city_set.filter(name__startswith="A")
		for city in cities:
			text_string += '%s <br>' % city.name



	return HttpResponse(text_string)


# def state_list(request, letter, sort):

#	states = State.objects.filter(name__startswith=letter).order_by(sort)

#	states_list=[]

#	for state in states:
#		states_list.append('%s <br>' % state.name)


#	return HttpResponse(states_list)