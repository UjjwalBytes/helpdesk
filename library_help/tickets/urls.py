from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-ticket/', views.create_ticket, name='create_ticket'),
    path('register/', views.register, name='register'),  # 👈 ADD THIS
    path('chatbot/', views.chatbot, name='chatbot'),
    path('edit-ticket/<int:ticket_id>/', views.edit_ticket, name='edit_ticket'),
]