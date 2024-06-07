from django.contrib.auth.models import \
    AbstractUser  # for using custom user model
from django.db import models


class User(AbstractUser):

    # fields

    username = models.CharField(max_length=200, unique=True)
    # null is false by default,

    def __str__(self):
        return self.username


class Entry(models.Model):

    # fields

    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_entry = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_entries"
    )
    # if the user is deleted, Entry also will be deleted

    # user - entry foreign key relationship
    class Meta:
        ordering = ["-created_entry"]
        verbose_name = "Entry"
        verbose_name_plural = "Entries"
