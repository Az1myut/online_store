from django import forms
<<<<<<< HEAD

class AddFileForm(forms.Form):
    file = forms.FileField(label='File',)
=======
from .models import BbCodeModel
class BbCodeForm(forms.ModelForm):
    class Meta:
        model = BbCodeModel
        fields = '__all__'
>>>>>>> b755f87e829ee1b394a3d1c7a5ae764b906e867e
