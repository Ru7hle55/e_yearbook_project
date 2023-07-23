from django.contrib import admin
from MYpetstagram.photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'photo_name',
        'date_of_publication',
        'description',
        'get_tagged_pets',
    )

    @staticmethod
    def photo_name(obj):
        return obj.photo.name

    @staticmethod
    def get_tagged_pets(obj):
        return ', '.join([pet.name for pet in obj.tagged_pets.all()])


# Register your models here.
admin.site.register(Photo, PhotoAdmin)