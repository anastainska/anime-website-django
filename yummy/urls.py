from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', AnimeListView.as_view(), name='animes'),
    path('home/', home_screen_view, name='home_screen'),
    path('anime/<int:pk>/', AnimeDetail.as_view(), name='anime'),
    path('create-anime/', AnimeCreate.as_view(), name='anime-create'),
    path('anime-update/<int:pk>/', AnimeUpdate.as_view(), name='anime-update'),
    path('anime-delete/<int:pk>/', AnimeDelete.as_view(), name='anime-delete'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('account/', account_view, name='account'),
    path('anime/<int:anime_id>/add_to_favorites/', favourite_add, name='favourite_add'),
    path('anime/<int:anime_id>/remove_from_favorites/', remove_from_favorites, name='remove_from_favorites'),
    path('favourites/', favourite_list, name='favourites'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
