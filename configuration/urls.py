from django.urls import include, path
from django.contrib import admin

from configuration import admin
from .import views

urlpatterns =[
    path('', views.connect, name='connect'),
    path('login/', views.signIn, name='signIn'),
    path('login/login/', views.signIn, name='signIn'),
    path('f',views.index,name='f'),
    path('genres/',views.list_genre,name='genres'),
    path('disconnect/', views.signOut, name='disconnect'),
    path('deleteD/<int:id>', views.deleteD, name='deleteD'),
    path('updateD/<int:id>', views.updateD,name='updateD'),
    path('updateD/updateD_action/<int:id>',views.updateD_action, name='updateD_action'),
    path('addD/', views.add, name='addD'),
    path('addD/add_diplome/', views.add_diplome, name='add_diplome'),
    path('genres/deleteG/<int:id>', views.deleteG, name='deleteG'),
     path('genres/updateG/<int:id>', views.updateG,name='updateG'),
     path('genres/updateG/updateG_action/<int:id>',views.updateG_action, name='updateG_action'),
     path('genres/addG/', views.addG, name='addG'),
    path('genres/addG/add_Genre/', views.add_Genre, name='add_Genre'),
    #path('admin/', admin.site.urls),
    #path('msg', views.msg),
    
   
]