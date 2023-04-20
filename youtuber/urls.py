from django.urls import path
from .views import youtuber_list, youtuber_detail

urlpatterns = [

    path('', youtuber_list),
    path('detail/<int:pk>/', youtuber_detail),

]