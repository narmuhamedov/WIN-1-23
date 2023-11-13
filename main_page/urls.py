from django.urls import path
from .views import film_list_view, film_list_detail_view

urlpatterns = [
    path('film_list/', film_list_view),
    path('film_list/<int:id>/', film_list_detail_view),
]
