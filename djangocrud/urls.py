
from django.contrib import admin
from django.urls import path
from tareas import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/',views.signup, name= 'signup'),
    path('tasks/', views.tasks, name= 'tasks'),
    path('logout/', views.signout, name='signout'),
    path('signin/', views.signin, name='signin'),

]
