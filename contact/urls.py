from django.urls import path
from contact.views import contact_us, detail

app_name = 'contact'

urlpatterns = [
    path('', contact_us, name='new'),
    path('<int:pk>/', detail, name='detail'),
]
