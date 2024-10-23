from django.urls import path
from utils.views import contact, chat

urlpatterns = [
    path('contact/', contact, name='contact'),
path('chat/', chat, name='chat')

]
