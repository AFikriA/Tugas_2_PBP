import imp
from django.urls import path
from todolist.views import delete_ajax, show_todolist, register, login_user, logout_user, create_task, delete, done, show_json, submit_ajax, show_todolist_ajax, delete_ajax, done_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('delete/<int:id>/', delete, name='delete'),
    path('done/<int:id>/', done, name='done'),
    path('json/', show_json, name="show_json"),
    path('/submit', submit_ajax, name="submit_ajax"),
    path('ajax/', show_todolist_ajax, name="show_todolist_ajax"),
    path('delete_ajax/<int:id>/', delete_ajax, name='delete_ajax'),
    path('done_ajax/<int:id>/', done_ajax, name='done_ajax'),
]