from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from tickets.views import custom_logout


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
     path('logout/', custom_logout, name='logout'),
    # path('register/', include('tickets.urls')),

    path('', include('tickets.urls')),
]