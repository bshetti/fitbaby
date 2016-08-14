from django.http import HttpResponse
from django.template import loader
from django.template.loader import get_template
from django.template import RequestContext
from .forms import PostForm
from django.views.decorators.csrf import csrf_protect

def index(request):
    template = get_template("polls/index.html")
    return HttpResponse(template.render())

@csrf_protect
def signup(request):
    template = get_template("polls/signup.html")
    
    form=PostForm()
    if form.is_valid():
	instance=form.save(commit=False)
        instance.firstname=form.cleaned_data['firstname']
	instance.lastname=form.cleaned_data['lastname']
	instance.email=form.cleaned_data['email']
	instance.save()
	return HttpResponseRedirect('/')
    
    context = RequestContext(request,{'form':form})
    return HttpResponse(template.render({'form':form}, request))


