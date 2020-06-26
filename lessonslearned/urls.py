from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from ll import views
from ll.views import projectnumber_upload, projectname_upload, client_upload, projectlocation_upload, marketsector_upload, memo_upload


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^chaining/', include('smart_selects.urls')),
    path('', include('ll.urls')),
    path('', include(('ll.urls', 'search'), namespace='search')),

    path('upload-projectnumber/', projectnumber_upload, name="projectnumber_upload"),
    path('upload-projectname/', projectname_upload, name="projectname_upload"),
    path('upload-client/', client_upload, name="client_upload"),
    path('upload-location/', projectlocation_upload, name="projectlocation_upload"),
    path('upload-market/', marketsector_upload, name="marketsector_upload"),
    path('upload-memo/', memo_upload, name="memo_upload"),
]
