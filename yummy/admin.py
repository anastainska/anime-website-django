from django.contrib import admin
from .models import User, Admin, Subscriber, Anime, MediaFile, Folder

# Register your models here.

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Subscriber)
admin.site.register(Anime)
admin.site.register(MediaFile)
admin.site.register(Folder)
