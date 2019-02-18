from django.contrib import admin
from .models import Post

#import post model to admin.py
#to prompt and edit Posts in Django Admin UI

admin.site.register(Post)