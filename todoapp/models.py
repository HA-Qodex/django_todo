from django.db import models
from django.forms import ModelForm


class TODOModel(models.Model):
    text = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text


class TODOForm(ModelForm):
    class Meta:
        model = TODOModel
        fields = ["text", ]
