from django.urls import path

from catalog.views import index_home, index_contacts

urlpatterns = [
    path('', index_home),path('contact/', index_contacts)
]
