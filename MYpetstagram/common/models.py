from django.db import models

from MYpetstagram.accounts.models import PetstagramUser
from MYpetstagram.photos.models import Photo


# Create your models here.
class Comment(models.Model):
    comment_text = models.TextField(
        blank=False,
        null=False,
        max_length=300,
    )
    date_and_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )
    to_photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(to=PetstagramUser, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-date_and_time_of_publication']


class Like(models.Model):
    to_photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(to=PetstagramUser, on_delete=models.CASCADE, null=True)