from django.contrib import admin

# Register your models here.s
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля которые должны отображаться в админке
    list_display = (
        'pk', 
        'text', 
        'pub_date', 
        'author',
        'group'
    )
    list_editable = ('group',)
    search_fields = ('text',) # Добавляем интерфейс для поиска по тексту постов
    list_filter = ('pub_date',) # Добавляем возможность фильтрации по дате
    empty_value_display = '-пусто-' # Это свойство сработает для всех колонок: где пусто — там будет эта строка 
    

# При регистрации модели Post источником конфигурации для неё назначаем класс PostAdmin
admin.site.register(Post, PostAdmin)
# регистрация модели Group возможно нужно добавить второй аргумент PostAdmin
admin.site.register(Group)