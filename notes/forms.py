from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django.forms import SplitDateTimeWidget
from  . import models


class NoteForm(ModelForm):
    class Meta:
        model = models.Note
        fields = (
            "title",
            'content',
        )

