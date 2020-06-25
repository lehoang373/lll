from . import views
from django.urls import path, re_path, include
from django.conf.urls import url

app_name = 'll'
urlpatterns = [
    path('', views.home, name='home'),
    path('signin', views.sign_in, name='signin'),
    path('signout', views.sign_out, name='signout'),
    path('callback', views.callback, name='callback'),

    path('lesson/create/', views.lesson_new, name='lesson_new'),
    path('lesson/<int:pk>/edit/', views.lesson_edit, name='lesson_edit'),
    path('lesson/<int:pk>/delete/', views.lesson_delete, name='lesson_delete'),
    url(r'^search/$', views.search, name='search'),
    path('export_lessons', views.export_Lessons_toCSV, name='export_lessons'),
]
