from django.urls import path
from .views import main_list_view, film_list_detail_view, create_review_film, premieres_view, SearchView

urlpatterns = [
    path('', main_list_view, name='film_list'),
    path('premieres/', premieres_view, name='premieres'),
    path('film_list/<int:id>/', film_list_detail_view),
    path('create-review/', create_review_film),
    path('search/', SearchView.as_view(), name='search')
]
