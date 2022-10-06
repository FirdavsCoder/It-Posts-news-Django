from django.urls import path
from .views import *

urlpatterns = [
    path('', main),
    path('<int:id>',post_detail),
   
]
