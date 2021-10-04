from django.forms import ModelForm
from .models import  Question


class add_question_form(ModelForm):
    class Meta:
        model=Question
        fields="__all__"