
from django.shortcuts import render
from django.http import HttpResponse
# from .models import Question
from django.template import Context, loader
from django.views.generic import TemplateView

def index(request):
	context = {'jason_is_dumb': True}
	return render(request, 'fundth/index.html', context)
