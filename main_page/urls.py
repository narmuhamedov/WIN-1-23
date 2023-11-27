from django.urls import path
from .views import film_list_view, film_list_detail_view, create_review_film

urlpatterns = [
    path('film_list/', film_list_view, name='film_list'),
    path('film_list/<int:id>/', film_list_detail_view),
    path('create-review/', create_review_film),
]
