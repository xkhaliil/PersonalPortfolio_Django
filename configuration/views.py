import ctypes
from .forms import FormConnexion
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User 
#from .forms import FormUser

from configuration.models import Diplome,Genre
def index (request):
   dip = Diplome.objects.all().values()
   gen=Genre.objects.all().values()
   template = loader.get_template('f.html')
   context = {
    'diplome': dip,
    'gen':gen,
   }
   return HttpResponse(template.render(context, request))

def list_genre(request):
    gen=Genre.objects.all().values()
    template = loader.get_template('genres.html')
    context = {
 'gen':gen,
 }
    return HttpResponse(template.render(context, request))

def connect (request):
    connect_form = FormConnexion ()
    return render(request, 'connexion.html', {'connect_form' : connect_form,'error':False})

def signIn(request):
    
    username = request.POST['login']
    password = request.POST['Mot_de_passe']
    #username = request.POST.get('login')
    #password = request.POST.get('mot2pass')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        request.session['username'] = username 
        return HttpResponseRedirect(reverse('f'))
 
    else:
        print("Login et/ou mot de passe incorrect")
        return render(request,'connexion.html', {'error':True,})
        


def signOut(request):
    logout(request) 
    return HttpResponseRedirect(reverse('main'))



def deleteD(request, id):
    dip = Diplome.objects.get(id=id)    
    dip.delete()
    return HttpResponseRedirect(reverse('f'))


def updateD(request, id):
    dip = Diplome.objects.get(id=id)
    gen = Genre.objects.all().values()
    template = loader.get_template('updateD.html')
    context = {
    'dip': dip,
    'gen':gen, }
    return HttpResponse(template.render(context, request))

def updateD_action(request, id):
    lib = request.POST['nomDiplome']
    p = request.POST['lieuDiplome']
    c = request.POST['gen']
    cat = Genre.objects.get(id=c)
    diplome = Diplome.objects.get(id=id)
    diplome.nomDiplome = lib
    diplome.lieuDiplome = p
    diplome.gen  = cat
    diplome.save()
    return HttpResponseRedirect(reverse('f'))

def add(request):
    gen = Genre.objects.all().values()
    template = loader.get_template('addD.html')
    context = {
    'gen': gen,
    }
    return HttpResponse(template.render(context, request))
def add_diplome(request):
    lib = request.POST['nomDiplome']
    p = request.POST['lieuDiplome']
    q = request.POST['dateDiplome']
    c = request.POST['gen']
    cat = Genre.objects.get(id=c)
    dip = Diplome(nomDiplome=lib, lieuDiplome=p, dateDiplome=q, gen=cat)
    dip.save()
    return HttpResponseRedirect(reverse('f'))

def deleteG(request, id):
    gen = Genre.objects.get(id=id)    
    gen.delete()
    return HttpResponseRedirect(reverse('genres'))

def updateG(request, id):
    gen = Genre.objects.get(id=id)
    template = loader.get_template('updateG.html')
    context = {
    # 'dip': dip,
    'gen':gen, }
    return HttpResponse(template.render(context, request))

def updateG_action(request, id):
    lib = request.POST['nomGenre']
    p = request.POST['descriptionGenre']
    gen = Genre.objects.get(id=id)
    gen.nomGenre = lib
    gen.descriptionGenre = p
    gen.save()
    return HttpResponseRedirect(reverse('genres'))
def addG(request):
    gen = Genre.objects.all().values()
    template = loader.get_template('addG.html')
    context = {
    'gen': gen,
    }
    return HttpResponse(template.render(context, request))
def add_Genre(request):
    lib = request.POST['nomGenre']
    p = request.POST['descriptionGenre']
    dip = Genre(nomGenre=lib, descriptionGenre=p)
    dip.save()
    return HttpResponseRedirect(reverse('genres'))

