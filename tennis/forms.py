from .models import Player
from django.forms import ModelForm, ValidationError


class AddPlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'nationality']

    def clean(self):
        cleaned_data = super(AddPlayerForm, self).clean()
        print(cleaned_data)
        print(cleaned_data.get('first_name'))
        first_name = cleaned_data.get('first_name').capitalize()
        last_name = cleaned_data.get('last_name').capitalize()
        try:
            Player.objects.get(first_name = first_name, last_name = last_name)
            raise ValidationError('This player with that name is already in the system')
        except Player.DoesNotExist:
                if first_name.isalpha() == False:
                    raise ValidationError('Player name can be letters only. Please run letters together.')
                elif last_name.isalpha() == False:
                    raise ValidationError('Player name can be letters only. Please run letters together.')
                else:
                    self.cleaned_data['first_name'] = first_name
                    self.cleaned_data['last_name'] = last_name
                    return cleaned_data

    