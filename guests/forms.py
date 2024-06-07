from django.forms import ModelForm

from .models import Entry


class EntryForm(ModelForm):

    class Meta:
        model = Entry
        fields = (
            "subject",
            "message",
            "user",
        )  # You can exclude 'user' since you're setting it in the view
