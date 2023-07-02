from django.forms import ModelForm
from .models import Pastry,Ingredients


class PastryForm (ModelForm) :
    class Meta :
        model = Pastry
        fields = "__all__"

class IngredientsForm (ModelForm) :
    class Meta :
        model = Ingredients
        fields ="__all__"

