from django.contrib import admin

from ads.models import Ad, Comment
from users.models import User


# TODO здесь можно подключить ваши модели к стандартной джанго-админке

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'role', 'image')
    list_filter = ('role',)
    search_fields = ('email',)
