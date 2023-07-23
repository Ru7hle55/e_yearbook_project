from django.contrib import admin
from MYpetstagram.common.models import Comment, Like


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'comment_text',
        'date_and_time_of_publication',
        'to_photo',
    )

# Register your models here.
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like)