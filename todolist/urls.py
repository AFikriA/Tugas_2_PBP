import imp
from django.urls import path
from todolist.views import delete, show_todolist, register, login_user, logout_user, create_task, delete, done

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('delete/<int:id>/', delete, name='delete'),
    path('done/<int:id>/', done, name='done'),
]