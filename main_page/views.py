from django.shortcuts import render, get_object_or_404, redirect
from .models import FilmListModel, Afisha, Slider
from . import forms
from django.urls import reverse


# Не полная информация
def film_list_view(request):
    if request.method == "GET":
        film_list = FilmListModel.objects.all()
        afisha_list = Afisha.objects.all()
        slider_list = Slider.objects.all()
        return render(request, template_name='films/index.html', context={
            'film_list': film_list,
            'afisha_list': afisha_list,
            'slider_list': slider_list
        })


# GET ID
def film_list_detail_view(request, id):
    if request.method == 'GET':
        film_id = get_object_or_404(FilmListModel, id=id)
        return render(request, template_name='films/film_detail.html', context={'film_id': film_id})


# create reviews
def create_review_film(request):
    if request.method == 'POST':
        form = forms.FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('film_list'))
    else:
        form = forms.FilmForm()
        return render(request, template_name='create_review.html', context={'form': form})
