from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from ll import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ll.urls')),
    path('', include(('ll.urls', 'search'), namespace='search')),
    path('microsoft/', include('microsoft_auth.urls', namespace='microsoft')),

    re_path(r'^accounts/login/$', LoginView.as_view(template_name='registration/login.html'), name="login"),
    re_path(r'^accounts/logout/$', LogoutView.as_view(), LogoutView.next_page, name="logout"),

    path('password_change_done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),
    path('password_reset_done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]
