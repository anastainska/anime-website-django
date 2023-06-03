from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from .models import Anime, Folder
from .forms import *


def home_screen_view(request):
    print(request.headers)
    return render(request, 'yummy/base.html', {})


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            account = form.save()
            login(request, account)
            return redirect('animes')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'yummy/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('animes')


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('animes')
    if request.POST:
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('animes')
    else:
        form = UserAuthenticationForm()

    context['login_form'] = form
    return render(request, 'yummy/login.html', context)


def account_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
                "date_of_birth": request.POST['date_of_birth']
            }
            form.save()
            context['success_message'] = "Updated changes! :)"
    else:
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
                "date_of_birth": request.user.date_of_birth
            }
        )
    context['account_form'] = form
    return render(request, 'yummy/account.html', context)


def favourite_add(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    folder, created = Folder.objects.get_or_create(id_subscriber=request.user.subscriber, name='Favourites')
    folder.favourites.add(anime)
    return redirect('anime', pk=anime_id)


def remove_from_favorites(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    folder = Folder.objects.get(name='Favourites', id_subscriber=request.user.subscriber)
    folder.favourites.remove(anime)
    return redirect('favourites')


def favourite_list(request):
    folder, created = Folder.objects.get_or_create(id_subscriber=request.user.subscriber, name='Favourites')
    favourites = folder.favourites.all()
    return render(request, 'yummy/favourites.html', {'favourites': favourites})


class AnimeListView(ListView):
    model = Anime
    context_object_name = 'animes'


class AnimeDetail(DetailView):
    model = Anime
    context_object_name = 'anime'


class AnimeCreate(CreateView):
    model = Anime
    fields = '__all__'
    success_url = reverse_lazy('animes')


class AnimeUpdate(UpdateView):
    model = Anime
    fields = '__all__'
    success_url = reverse_lazy('animes')


class AnimeDelete(DeleteView):
    model = Anime
    context_object_name = 'anime'
    success_url = reverse_lazy('animes')
