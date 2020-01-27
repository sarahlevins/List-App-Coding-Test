from .models import Player
from django.forms import ModelForm, ValidationError


class AddPlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'nationality']
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name.isalpha() == False:
            raise ValidationError("Player name can be letters only. Please run letters together.")
        else:
            first_name = self.cleaned_data['first_name']
            return first_name.capitalize()

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if last_name.isalpha() == False:
            raise ValidationError("Player name can be letters only. Please run letters together.")
        else:
            last_name = self.cleaned_data['last_name']
            return last_name.capitalize()
    

    