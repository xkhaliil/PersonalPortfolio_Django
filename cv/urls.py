from django.urls import path

from configuration import admin
from .import views

urlpatterns =[
    path('main/',views.index,name='main'),
    path('d/',views.diplomes,name='d'),
    path('s/',views.stages,name='s'),
    path('c/',views.competences,name='c'),
    path('', views.message, name='message'),
    #path('admin/', admin.site.urls),

    

]