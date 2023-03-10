from django.shortcuts import render
from tempfile import template
from urllib import request
from django.http import HttpResponse
from django.template import loader

def index (request):
      template =loader.get_template('main.html')
      context = {
    'type': 'Etudiant',
      }   
      return HttpResponse (template.render(context, request))

from configuration.models import Diplome
def diplomes (request):
       diplome = Diplome.objects.all().values()
       template = loader.get_template('d.html')
       context = {
        'diplome': diplome,
 }
       return HttpResponse(template.render(context, request))

from configuration.models import Stage
def stages (request):
       stage = Stage.objects.all().values()
       template = loader.get_template('s.html')
       context = {
 'stage': stage,
 }
       return HttpResponse(template.render(context, request))

from configuration.models import Competence
def competences (request):
       competence = Competence.objects.all().values()
       template = loader.get_template('c.html')
       context = {
 'competence': competence,
 }
       return HttpResponse(template.render(context, request))

def message(request):
 return HttpResponse("hammamet")

